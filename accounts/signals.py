from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import User
from datetime import datetime


# @receiver(post_save, sender=User)
# def set_created(sender, **kwargs):
#     if kwargs['created']:
#         pk = kwargs['instance'].id

#         User.objects.filter(pk=pk).update(created=F('points')+5)

#         user_instance = kwargs['instance']
#         user_instance.created = datetime.now().timestamp()
#         user_instance.save()
#         print(f'{user_instance.created} is set')
