from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def index_v(request):
    html = 'index.html'
    return render(request, html)


def error_v(request):
    html = "error.html"
    return render(request, html)
