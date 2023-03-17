from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, logout_then_login,
    PasswordChangeView as AuthPasswordChangeView,
)
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

# from .forms import SignupForm, ProfileForm, PasswordChangeForm
from .forms import SignupForm
from .models import User

login = LoginView.as_view(template_name="accounts/login_form.html")


# def logout(request):
#     messages.success(request, '로그아웃되었습니다.')
#     return logout_then_login(request)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
        #     auth_login(request, signed_user)
            messages.success(request, "Congratulation!")
        #     signed_user.send_welcome_email()  # FIXME: Celery로 처리하는 것을 추천.
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })