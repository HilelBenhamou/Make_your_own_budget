from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import User
from account.models import Transaction

# Create your views here.


def home(request):
    return render(request, 'user/home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def my_profile(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'user/my_profile.html', {'user': user})

