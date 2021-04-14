from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

