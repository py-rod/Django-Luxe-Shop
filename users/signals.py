from django.shortcuts import redirect
from allauth.account.signals import user_signed_up, email_added
from django.dispatch import receiver


@receiver(user_signed_up)
def activate_user(sender, request, user, **kwargs):
    user.is_active = True
    user.save()
