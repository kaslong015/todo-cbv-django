from django.shortcuts import render,redirect
from  django.views.generic import ListView,DetailView,FormView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from core.models import Task
from core.forms import TaskForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name ='core/login.html'

    def get_redirect_url(self):
        return reverse_lazy('list-task')



class ListTask(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_nam = 'task'


class CreateTask(LoginRequiredMixin,FormView):
    model = Task
    form_class = TaskForm
    success_url =  reverse_lazy('list-task')
    template_name = 'core/form.html'

    def form_valid(self,form):
        # form.instance.user =self.request.user
        form.save()
        return super().form_valid(form)


class UpdateTask(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('list-task')
    template_name = 'core/form.html'


class DeleteTask(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('list-task')


class CreataUserView(FormView):
    template_name = 'core/task_create.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self,form):
        user = form.save()
        # if user is not None:
        #     return reverse_lazy('login')
        return super(CreataUserView,self).form_valid(form)


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('list-task'))
        return super(RegisterPage, self).get(*args, **kwargs)
