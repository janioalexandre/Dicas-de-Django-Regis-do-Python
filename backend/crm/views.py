from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.conf import settings
from django.views.decorators.http import require_http_methods

from .forms import ContactForm

@require_http_methods(['POST'])
def send_contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        try:
            send_mail(
                subject=form.cleaned_data['title'],
                message=form.cleaned_data['body'],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('core:index')
        except Exception as e:
            print(f'Erro ao enviar email: {e}')
            
    return render(request, 'contact.html', {'form': form})