from django.shortcuts import render, redirect
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.decorators import login_required
from accounts.forms import QuizAuthenticationForm, EmailUserCreationForm

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            next_url = request.GET.get('next', 'shop:index')
            return redirect(next_url)
    else:
        form = EmailUserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')