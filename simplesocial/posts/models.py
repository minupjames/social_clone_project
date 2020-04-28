from django.conf import settings
from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=True)
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,related_name="posts",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
        
    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('posts:post_detail',kwargs={'pk':self.pk,
                                            'username':self.user.username})
                                            
    class Meta:
        ordering = ['-created_at']
        unique_together = ['message','user']