from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
User = get_user_model()

import logging

logger = logging.getLogger(__name__)

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'home.html'

class StarSocialLogin(TemplateView):
    template_name = 'login_starsocial.html'
    model = User


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
