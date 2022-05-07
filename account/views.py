from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import RegisterForm, ProfileUpdateForm
from .models import Account
from blog.views import BaseView


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


class UserProfile(View):
    def get(self, request):
        username = request.user.username
        profile = Account.objects.get(username=username)
        context = {
            'profile': profile
        }

        return render(request, 'account/profile.html', context)


class UserUpdate(UpdateView, BaseView):
    model = Account
    form_class = ProfileUpdateForm
    template_name = 'account/user_update.html'
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return context