from django.shortcuts import render
from base.forms import UserRegisterForm

# Create your views here.
def base(request):
    context = {

    }
    return render(request, 'base/base.html', context)


def register(request):
    if request.POST:
        form = UserRegisterForm(request.POST)

    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'base/register.html', context)