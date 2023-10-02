import random
import string

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class LoginView(BaseLoginView):
    pass


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # Сохранение объекта перед тем, как установить ему пароль
        token = ''.join(random.sample(string.digits + string.ascii_letters, 12))
        self.object.token = token
        self.object.is_active = False
        self.object.save()
        url = f'''http://127.0.0.1:8000/users/verify/{token}'''

        if form.is_valid():
            send_mail(
                subject='Подтверждение регистрации',
                message=f'''Вы успешно зарегистрировались, чтобы подтвердить почту перейдите по ссылке {url}.''',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email]
            )
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def verify_email(request, token):
    user = User.objects.filter(token=token).first()
    if user is not None:
        user.is_active = True
        user.save()
        return redirect('users:login')
    # return render(request, 'users/verify_email.html')


def reset_password(request):
    if request.method == 'POST':
        input_email = request.POST.get('email')
        user = User.objects.filter(email=input_email).first()
        password = ''.join(random.sample(string.digits + string.ascii_letters, 12))
        user.set_password(password)
        user.save()
        send_mail(
            subject='Сброс пароля',
            message=f'''Вы успешно сбросили пароль для аккаунта {input_email}.\n Ваш новый пароль: {password}''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[input_email]
        )

    return render(request, 'users/reset_password.html')
