from celery import shared_task
import datetime
from news.models import Post, Category
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

@shared_task
def weekly_notify():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time__gte=last_week)
    categories = set(posts.values_list('category__category', flat=True))
    subscribers = set(Category.objects.filter(category__in=categories).values_list('subscribers__email', flat=True))
    print("выполняю")
    html_content = render_to_string(
        'daily_post.html',
        {
            'link' : settings.SITE_URL,
            'posts' : posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Статьи за прошедшую неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@shared_task
def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text':f'{preview[0:50]}...',
            'link':f'{settings.SITE_URL}/posts/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()