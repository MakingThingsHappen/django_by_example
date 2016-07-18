from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image


@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        instance.total_likes += 1
        instance.save()
    elif kwargs['action'] == 'post_remove':
        instance.total_likes -= 1
        instance.save()

