from django.shortcuts import render
from django.views.generic import CreateView, FormView, UpdateView, TemplateView
from django.urls import reverse_lazy, reverse
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, redirect


class LoginView(TemplateView):

    success_url = reverse_lazy('inicio')
    template_name = 'login.html'

    def post(self, request):
        username = self.request.POST.get('username', '')
        password = self.request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return(redirect('inicio'))
            else:
                return render_to_response("login.html",
                                          {'invalid': True})
        else:
            return render_to_response("login.html",
                                      {'invalid1': True})
