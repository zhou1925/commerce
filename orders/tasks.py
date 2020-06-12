from __future__ import absolute_import, unicode_literals
from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'order nr {order_id}'
    message = f'Dear {order.first_name} your order ID is {order.id}'
    mail_sent = send_mail(subject,
                          message,
                          'admin@admin.com',
                          [order.email])

    return mail_sent