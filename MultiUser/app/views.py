from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
def Signup(request):
    if request.method == 'POST':
       username =request.POST.get('username')
       password = request.POST.get('password')
       user =User.objects.create_user(username=username,password=password)
       user.save()
       return redirect('/login')
    return render(request, 'signup.html')

def Login(request):
     if request.method == 'POST':
         username =request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)
         if user is not None:
             login(request, user)
             return redirect('/todo')
         else:
             return redirect('/login')

     return render(request, 'login.html')


@login_required
def Todoview(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        describtion = request.POST.get('describtion')

        if title and describtion:
            Todo.objects.create(
                title=title,
                describtion=describtion,
                user=request.user
            )
        return redirect('/todo')

    res = Todo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})


@login_required
def edit_todo(request, id):
    todo = get_object_or_404(Todo, srno=id, user=request.user)

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.describtion = request.POST.get('describtion')
        todo.save()
        return redirect('/todo')

    return render(request, 'edit_todo.html', {'todo': todo})


@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, srno=id, user=request.user)
    todo.delete()
    return redirect('/todo')
