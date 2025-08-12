from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect
from django.utils.datastructures import MultiValueDictKeyError


def home(request):
    return render(request, "home.html")


def todo(request):
    return render(request, "todo.html")
