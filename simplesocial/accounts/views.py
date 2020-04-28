from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from . import forms



class SignUpPage(CreateView):
    form_class =forms.UserCreateForm
    template_name='accounts/sign_up.html'
    success_url = reverse_lazy('accounts:login')