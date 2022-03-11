from unicodedata import name
from django.urls import path
from . import views
from .views import Cadastro, CadastroCreate, CadastroUpdate


app_name = 'forum'

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("topicos/", views.TopicosPageView.as_view(), name="topicos"),
    path('cadastrar/', views.CadastroCreate.as_view(), name='cadastro'),
    path('editar/cadastro/<int:pk>/', CadastroUpdate.as_view(), name='editar-Cadastro'),
]
