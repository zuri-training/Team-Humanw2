from django.shortcuts import render

from django.view.generic import TemplateView

class SignUpView(TemplateView):
	template_name = 'signup.html'
class HomeView(TemplateView):
	template_name = 'home.html'
class LoginView(TemplateView):
	template_name = 'login.html'
class LogoutView(TemplateView):
	template_name ='logged_out.html'
class PassEmailView(TemplateView):
	template_name = 'password_reset_email.html'
class PassFormView(TemplateView):
	template_name = 'password_reset_email.html'
class PassCompleteView(TemplateView):
	template_name = 'password_reset_complete.html'
