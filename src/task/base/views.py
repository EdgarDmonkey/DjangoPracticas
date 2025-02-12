from django.shortcuts import render, redirect # type: ignore
from django.views.generic.list import ListView # type: ignore
from django.views.generic.detail import DetailView # type: ignore
from .models import task
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth import login # type: ignore
from django.contrib.auth.views import LoginView # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin # type: ignore
from django.urls import reverse_lazy # type: ignore

# Create your views here.

class Logueo(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('main')
    

class PaginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(PaginaRegistro, self).form_valid(form)
    
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super(PaginaRegistro,self).get(*args, **kwargs)
     

class ListaPendientes(LoginRequiredMixin, ListView):
    model = task
    context_object_name = 'Tareas'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tareas'] = context['Tareas'].filter(user=self.request.user)
        context['count'] = context['Tareas'].filter(done=False).count()
        
        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['Tareas'] = context['Tareas'].filter(title__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context 
        
class DetalleTarea(LoginRequiredMixin, DetailView):
    model = task
    context_object_name = 'Tarea'
    template_name = 'base/detalles.html'
    

class CrearTarea(LoginRequiredMixin, CreateView):
    model = task
    fields = ['title', 'description', 'done']
    success_url = reverse_lazy('main')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CrearTarea, self).form_valid(form)
        


class EditarTarea(LoginRequiredMixin, UpdateView):
    model = task
    fields = ['title', 'description', 'done']
    success_url = reverse_lazy('main')
    

class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = task
    context_object_name = 'Tarea'
    success_url = reverse_lazy('main')