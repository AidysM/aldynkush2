from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.signing import BadSignature
from django.contrib.auth import logout
from django.contrib import messages

from .models import AdvUser
from .forms import ChangeUserInfoForm, RegisterUserForm
from .utilities import signer


def index(request):
    return render(request, 'home/index.html')

def about_page(request, page):
    try:
        template = get_template('home/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

def contact_page(request, page):
    try:
        template = get_template('home/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

class AKLoginView(LoginView):
    template_name = 'home/login.html'

@login_required
def profile(request):
    return render(request, 'home/profile.html')

class AKLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'home/logout.html'

class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'home/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('home:profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class AKPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'home/password_change.html'
    success_url = reverse_lazy('home:profile')
    success_message = 'Пароль пользователя изменен'

class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'home/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home:register_done')

class RegisterDoneView(TemplateView):
    template_name = 'home/register_done.html'

def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'home/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'home/user_is_activated.html'
    else:
        template = 'home/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)

class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'home/delete_user.html'
    success_url = reverse_lazy('home:index')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super(DeleteUserView, self).setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
        return super(DeleteUserView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

