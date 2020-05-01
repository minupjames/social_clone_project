from django import forms

from .models import Post
import logging

logger = logging.getLogger(__name__)

class PostForm(forms.ModelForm):
    class Meta:
        fields = ("message", "group")
        model = Post
    def __init__(self, *args, **kwargs):
        logger.info('sfs')
        user = kwargs.pop("user", None)
        super(PostForm, self).__init__(*args, **kwargs)
        if user is not None:
           self.fields["group"].queryset = (
               models.Group.objects.filter(
                   pk__in=user.groups.values_list("group__pk")
               )
           )
