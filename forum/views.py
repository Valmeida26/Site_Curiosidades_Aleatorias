from django.shortcuts import render
# Create your views here.
from forum.models import Post
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Cadastro



def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


class HomePageView(TemplateView):
    template_name = "home.html"


class TopicosPageView (TemplateView):
    posts = Post.objects.all()
    template_name = "topicos.html"


class EditPageView (TemplateView):
    template_name = "edit.html"


class CadastroCreate(CreateView):
    model = Cadastro
    fields = ['nome', 'sobrenome', 'sexo', 'nascimento']
    template_name = 'cadastro/form.html'
    context_0bject_name = 'cadastro'    


class CadastroUpdate(UpdateView):
    model = Cadastro
    fields = ['nome', 'sobrenome', 'sexo']
    template_name = 'cadastro/form.html'
    context_0bject_name = 'cadastro' 


#class CadastroDelete(DeleteView):
   # model = Cadastro
    #template_name = 'cadastro/form-excluir.html'
   # context_0bject_name = 'cadastro' 

    

    
    
    






