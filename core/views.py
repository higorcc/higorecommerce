from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import CreateView, TemplateView
from django.contrib import messages
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
    elif request.method == 'POST':
        messages.error(request, 'Formulário Inválido')
    context = {
        'form': form,
        'success': success
        }
    return render(request, 'contact.html', context)


