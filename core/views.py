from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import View, TemplateView
# Create your views here.

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




