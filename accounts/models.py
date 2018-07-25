from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from django.shortcuts import redirect


class Profile(models.Model):
    EXPERIENCE_CHOICES = (
        ('less than 1 year', 'less than i year'),
        ('1 to 3 years', '1 to 3 years'),
        ('more than 3 year', 'more than 3 year')
    )
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    career = models.CharField(max_length=200, blank=True)


@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    #instance.profile.save()


