from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    image=models.ImageField(upload_to="profiles")

    def __str__(self):
        return self.user.username
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    """Create a new profile when a new user is added"""
    if created:
        Profile.objects.create(user=instance)