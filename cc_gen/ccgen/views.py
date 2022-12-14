 
from django.urls import reverse_lazy
from django.shortcuts import render
 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Download,Comment,Design
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from .forms import  usersignupform, designForm
import datetime
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, 'ccgen/index.html')


class userCreateview(CreateView):
    form_class=usersignupform
    template_name='ccgen/signup.html'

    def form_valid(self, form):
        user=User.objects.create_user(email=self.request.POST['email'], username=self.request.POST['username'], password=self.request.POST['password'], )
        return redirect('ccgen:index')
 
    
class designListView(generic.ListView):
    model=Design
    context_object_name='design_list'
    template_name='ccgen/design_list.html'
    
    def get_queryset(self):
        return Design.objects.all()

class designDetailView(generic.DetailView):
    model=Design
    template_name='ccgen/design_detail.html'

class designCreate(CreateView):
    model=Design
    form_class=designForm
    successful_url=reverse_lazy('ccgen:index')


class designDelete(DeleteView):
    model=Design
    success_url=reverse_lazy('ccgen:designs')
    
class downloadedListView(LoginRequiredMixin, generic.ListView):
    model=Download
    context_object_name='download_list'
    template_name='ccgen/downloaded_list.html'
    
    def get_queryset(self):
        return Download.objects.filter(user=self.request.user).filter(downloaded=True)

class savedfordownloadListView(LoginRequiredMixin, generic.ListView):
    model=Download
    context_object_name='willdownload_list'
    template_name='ccgen/saved_list.html'
    
    def get_queryset(self):
        return Download.objects.filter(user=self.request.user).filter(downloaded=False)

class dashboard(generic.DetailView):
    model=User
    template_name='ccgen/dashboard.html'
