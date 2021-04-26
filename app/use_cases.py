from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *


def create_user_case(request=None):
    if request is None:
        return SignupForm().fields

    form = SignupForm(request.POST, request.FILES)
    if form.is_valid():
        user = form.save()
        login(request, user)
    else:
        user = form.errors
    return user.profile

def login_user_case(request=None, data=None):
    if data is None:
        return LoginForm().fields

    form = LoginForm(data)
    if form.is_valid():
        user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(request, user)
    else:
        user = form.errors
    return user.profile

def logout_user_case(data):
    logout(data)