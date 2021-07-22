from django.shortcuts import render, redirect
from .models import Cart_list
from django.urls import reverse_lazy
from .forms import Cart_listForm, EditCart_listForm
#CBV
from django.views.generic import FormView,  ListView,  CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#mixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class CartListView(LoginRequiredMixin,ListView):
    model = Cart_list
    context_object_name = 'item'
    template_name='shopping/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item"] = context['item'].filter(user=self.request.user)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['item'] = context['item'].filter(
                date__startswith=search_input)
        context['search_input'] = search_input
        return context



class CreateGroceryListView(LoginRequiredMixin,CreateView):
    model = Cart_list
    template_name = "shopping/add_list.html"
    #fields  ='__all__'
    success_url = reverse_lazy('index')
    form_class = Cart_listForm
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(CreateGroceryListView,self).form_valid(form)
    


class UpdateGroceryListView(LoginRequiredMixin,UpdateView):
    model = Cart_list
    template_name = "shopping/update_list.html"
    #fields = '__all__'
    success_url = reverse_lazy('index')
    form_class = EditCart_listForm

class DeleteGroceryListView(LoginRequiredMixin,DeleteView):
    model = Cart_list
    template_name = "shopping/confirm_delete.html"
    success_url = reverse_lazy('index')

class CartLogin(LoginView):
    template_name = 'shopping/login.html'
    #fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class CartLogout(LoginRequiredMixin,LogoutView):
        next_page = 'index'	
        #success_url= redirect('index')


class Register(CreateView):
    template_name = 'shopping/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
    
        return super(Register,self).form_valid(form)
    
