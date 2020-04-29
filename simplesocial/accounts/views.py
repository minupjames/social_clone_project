from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms

import logging

logger = logging.getLogger(__name__)


class SignUpPage(CreateView):
    form_class =forms.UserCreateForm
    template_name='accounts/sign_up.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.POST.get('username')
        super(SignUpPage, self).form_valid(form)
        logger.info('Created: %s', obj.created_by)
        return super(SignUpPage, self).form_valid(form)
        #return reverse_lazy('starsocial_login', kwargs={'name': obj.created_by})

    def get_success_url(self, **kwargs):
        logger.info('kwargs: %s', self.object.username)
        name = self.object.username
        return reverse_lazy('starsocial_login', kwargs={'name': name})

    """def post(self, request, *args, **kwargs):
        name = request.POST.get('username')
        logger.info('name:%s', request.POST.get('username'))
        #success_url = reverse_lazy('starsocial_login')
        return render(request, 'login_starsocial.html', {'name': name})
        #return render(request, 'login_starsocial.html')"""
