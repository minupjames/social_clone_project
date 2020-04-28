from django.shortcuts import render
from django.views import generic
from django.contrib import messages                                       
from .models import Group, GroupMember
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ListGroups(generic.ListView):
    model = Group
    
    
class GroupDetail(generic.DetailView):
    model = Group
    
class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name','description')
    model = Group
    
class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:group_detail",kwargs={"slug": self.kwargs.get("slug")})
  
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(group.name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.name))

        return super().get(request, *args, **kwargs)
        
class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:group_detail",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
            ).get()

        except models.GroupMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )

        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )
        return super().get(request, *args, **kwargs)
