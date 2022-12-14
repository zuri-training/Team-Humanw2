from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import usersignupform
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your views here.
#@login_required
def index(request):
    return render(request, 'ccgen/index.html')


class userCreateview(CreateView):
    form_class=usersignupform
    template_name='ccgen/signup.html'

    def form_valid(self, form):
        user=User.objects.create_user(email=self.request.POST['email'], username=self.request.POST['username'], password=self.request.POST['password'], )
        return redirect('ccgen:index')
