from django.shortcuts import render, redirect
from .forms import CreateUserForm


# Create your views here.
def register(response):
    if response.method == 'POST':
        form = CreateUserForm(response.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('Invalid')
    else:
        form = CreateUserForm()
    return render(response, 'register/register.html', {"form": form})