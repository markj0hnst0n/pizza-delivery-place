from django.shortcuts import render
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
        user_name = request.POST.get("name")
        query = request.POST.get("query")
        order_number = request.POST.get("order_number")

        if order_number == "":
            shop_subject = render_to_string(
                'home/contact_emails/shop_contact_subject_no_order.txt')
        else:
            shop_subject = render_to_string(
                'home/contact_emails/shop_contact_subject_order.txt',
                {'order_number': order_number})

        shop_body = render_to_string(
            'home/contact_emails/shop_contact_body.txt',
            {'user_name': user_name, 'query': query})

        customer_subject = render_to_string(
            'home/contact_emails/contact_email_subject.txt')
        customer_body = render_to_string(
            'home/contact_emails/contact_email_body.txt')

        send_mail(
            shop_subject,
            shop_body,
            user_email,
            [settings.DEFAULT_FROM_EMAIL]
        )

        send_mail(
            customer_subject,
            customer_body,
            settings.DEFAULT_FROM_EMAIL,
            [user_email]
        )
        messages.info(request, "Contact form sent")

    return render(request, 'home/contact.html')


def error_400_view(request, exception):
    messages.error(request, 'Bad request')
    return render(request, 'home/400.html')


def error_403_view(request, exception):
    messages.error(request, 'Forbidden')
    return render(request, 'home/403.html')


def error_404_view(request, exception):
    messages.error(request, 'Page not found')
    return render(request, 'home/404.html')


def error_500_view(request):
    messages.error(request, 'Server problem')
    return render(request, 'home/500.html')
