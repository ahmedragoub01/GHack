from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    reset_password_token = models.CharField(max_length=50, blank=True, default="")
    reset_password_expire = models.DateTimeField(null=True, blank=True)
    activation_token = models.CharField(max_length=50, blank=True, default="")
    activation_token_expire = models.DateTimeField(null=True, blank=True)
    is_email_confirmed = models.BooleanField(default=False)

    @property
    def is_activation_token_expired(self):
        if self.activation_token_expire:
            return self.activation_token_expire < timezone.now()
        return True

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

