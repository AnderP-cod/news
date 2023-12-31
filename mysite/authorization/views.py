from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            for error_list in form.errors.values():
                for error in error_list:
                    messages.warning(request, error)
    else:
        form = SignUpForm()
    return render(request, 'auth.html', {'form': form, 'title': 'Sign up'})
