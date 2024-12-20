from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)