from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin


class InicioView(LoginRequiredMixin, TemplateView):

    template_name = 'inicio.html'
