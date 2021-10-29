from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.core.mail import send_mail
from .forms import ContactForm
#import models

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }

    return render(request, 'index.html', context)

def single_post(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            where_from = form.cleaned_data['where_from']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(where_from)
        # send an email
        message_main = f'name: {name} \n email: {email} \n website: {website} \n message: {message} '
        send_mail(
            subject, # subject
            message_main, # message
            '', # from email
            ['ebonnee.hoggard@gmail.com'], # To email
        )
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def work(request):
    return render(request, 'work.html')