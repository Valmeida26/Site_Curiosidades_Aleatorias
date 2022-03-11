from django.contrib import admin

# Register your models here.
from .models import Post, Cadastro

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_created", "updated")

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ("nome", "sobrenome", "sexo", "nascimento")



