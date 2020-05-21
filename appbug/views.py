from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from appbug.models import CustomUser
from appbug.forms import login_f, user_f


def index_v(request):
    html = 'index.html'
    return render(request, html)


def error_v(request):
    html = "error.html"
    return render(request, html)


# def register_v(request):
#     html = "form.html"
#     if request.method == "POST":
#         form = user_f(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             CustomUser.objects.create_user(
#                 username=data['username'],
#                 password=data['password'],
#             )
#             user = authenticate(
#                 request, username=data['username'], password=data['password'])
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     form = user_f()
#     return render(request, html, {'form': form})


def login_v(request):
    if request.method == "POST":
        form = login_f(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home')))
    form = login_f()
    return render(request, 'form.html', {'form': form})


def logout_v(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    pass


@ login_required
def home_v(request):
    html = 'home.html'
    user = request.user
    return render(request, html, {'user': user})
