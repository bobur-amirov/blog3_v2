from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegisterForm
from .models import Account


class LoginView(View):
    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog_list')


class RegisterView(CreateView):
    model = Account
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')
