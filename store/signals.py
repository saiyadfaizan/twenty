'''from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from ecom.store.models import Customer

@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)
'''