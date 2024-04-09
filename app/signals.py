from django.db.models.signals import post_save
from django.dispatch import receiver
import time


@receiver(post_save, sender='app.test') 
def testing(sender, instance, **kwargs):
    from .models import test, after_test
    print("executed the post_save signal before sending the response to the user")
    time.sleep(2)