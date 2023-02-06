from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user_instance = instance
        profile = Profile.objects.create(
            user=user_instance,
            username=user_instance.username,
            email=user_instance.email,
            name=user_instance.first_name,
        )

        subject = 'Welcome to Devsearch :D'
        message = 'We are glad you are here!'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
        )


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


# post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(profileDeleted, sender=Profile)


@receiver(post_save, sender=Profile)
def editUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
