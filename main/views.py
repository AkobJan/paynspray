from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from .forms import ContactForm

def index(request):
    form = ContactForm()
    return render(request, 'index.html',{'form': form})


def register(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})



def about_us(request):
    return render(request, 'about_us.html')

def contacts(request):
    return render(request, 'contacts.html')
