from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from appbug.models import CustomUser, Bug
from appbug.forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm, AddBugForm


def index_v(request):
    html = 'index.html'
    return render(request, html)


def error_v(request):
    html = "error.html"
    return render(request, html)


# def register_v(request):
#     html = "form.html"
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
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
#     form = CustomUserCreationForm()
#     return render(request, html, {'form': form})


def login_v(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, 'form.html', {'form': form})


def logout_v(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    pass


@ login_required
def home_v(request):
    html = 'home.html'
    user = request.user
    # bugs = Bug.objects.all().order_by('-date')
    new = Bug.objects.filter(status='N').order_by('-date')
    in_progress = Bug.objects.filter(status='P').order_by('-date')
    done = Bug.objects.filter(status='D').order_by('-date')
    invalid = Bug.objects.filter(status='I').order_by('-date')
    return render(request, html, {'user': user, 'new': new, 'in_progress': in_progress, 'done': done, 'invalid': invalid})


@ login_required
def bug_v(request, id):
    html = "bug_details.html"
    bug = Bug.objects.get(id=id)
    return render(request, html, {'bug': bug})


@ login_required
def user_v(request, id):
    html = "user_details.html"
    user = CustomUser.objects.get(id=id)
    assigned = Bug.objects.filter(owner=id).order_by('-date')
    filed = Bug.objects.filter(author=id).order_by('-date')
    completed = Bug.objects.filter(closer=id).order_by('-date')
    return render(request, html, {'user': user, 'assigned': assigned, 'filed': filed, 'completed': completed})


@login_required
def addbug_v(request):
    html = "form.html"

    if request.method == 'POST':
        form = AddBugForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Bug.objects.create(
                title=data['title'],
                description=data['description'],
                author=request.user,
                status='N'
            )
            # return HttpResponseRedirect(reverse('bug', kwargs={'id': Bug.objects.get('title' == data['title']).id}))
            return HttpResponseRedirect(reverse('home'))

    form = AddBugForm()

    return render(request, html, {"form": form})
