from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages

from django.conf import settings


def index(request):
    """ Returns Index/Homepage """
    return render(request, 'home/index.html')

def about(request):
    """ Shows about page for the business """
    return render(request, 'home/about.html')

def contact(request):
    """ Shows and allows user to sent contact form """
    if request.method == 'POST':
        user_email = request.POST.get("email")
        subject = render_to_string(
            'home/contact_emails/contact_email_subject.txt')
        body = render_to_string(
            'home/contact_emails/contact_email_body.txt')

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            user_email
        )
        messages.success(request, "Contact From Sent")

    return render(request, 'home/contact.html')