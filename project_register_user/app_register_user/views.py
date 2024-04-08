from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'users/home.html')

def users(request):
    #salvador os dados do input como novo usuário no banco de dados
    new_user = User() 
    new_user.name = request.POST.get('name')
    new_user.age = request.POST.get('age')
    new_user.save()
    #retorna a lista de usuários em uma nova página 
    #dentro de um dicionário 
    users = {
        'users': User.objects.all()
    }
    return render(request, 'users/users.html', users)
