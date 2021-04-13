from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

class IndexView(TemplateView):

    template_name = 'index.html'

index = IndexView.as_view()

def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    else:
        form = ContactForm()
    context = {
        'form': form,
        'success': success
        }
    return render(request, 'contact.html', context)


