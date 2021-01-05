import datetime

import pytz
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from .forms import UserRegisterForm
from .models import *
from dateutil.relativedelta import relativedelta

#################### index#######################################
from .models import Client


class index(ListView):
    model = Client
    paginate_by = 10


def index(request):
    newspapers = NewsPaper.objects.all()
    paginator = Paginator(newspapers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'user/index.html', {'title': 'index', 'page_obj': page_obj})


def profile(request):
    newspapers = NewsPaper.objects.all()
    paginator = Paginator(newspapers, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'user/profile.html', {'title': 'profile', 'page_obj': page_obj})


def newspaper(request, pk):
    newspaperObj = NewsPaper.objects.get(id=pk)
    return render(request, 'user/newspaper.html', {'title': 'newspaper', 'newspaper': newspaperObj})


def subscription(request, pk):
    if request.method == 'POST':
        duration = request.POST.get('duration')
        newspaperObj = NewsPaper.objects.get(id=pk)
        clientId = request.user
        today = datetime.date.today()
        endDate = today + relativedelta(months=int(duration))
        obj = Subscription()
        obj.client_id = clientId.id
        obj.newspaper_id = newspaperObj.id
        obj.price = newspaperObj.price
        obj.duration = duration
        obj.startDate = str(today)
        obj.endDate = str(endDate)
        obj.save()
        messages.success(request, 'Подписка оформлена!!')
        return redirect('index')


########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            obj = Client()
            obj.email = form.cleaned_data['email']
            obj.address = form.cleaned_data['address']
            obj.first_name = form.cleaned_data['first_name']
            obj.last_name = form.cleaned_data['last_name']
            obj.phone_number = form.cleaned_data['phone_no']
            obj.save()
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'reqister here'})


################ login forms###################################################
def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'log in'})
