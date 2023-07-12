from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode

from config import settings


def send_mail_for_verify(request, user):
    current_site = get_current_site(request)
    from django.utils.encoding import force_bytes
    context = {
        'user': user,
        'domain': current_site.domain,
        'token': default_token_generator.make_token(user),
        'uid': urlsafe_base64_encode(force_bytes(user.pk))
    }
    message = render_to_string(
        'users/verify_email.html',
        context=context,
        )

    email = EmailMessage(
        'Верификация учетной записи',
        message,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
        )
    email.send()