from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.cache import cache
from django.utils.translation import pgettext_lazy
from django.utils.translation import gettext as _


class Author(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def update_rating(self):
        post_rating = 0 
        comments_rating = 0
        post_comments_rating = 0
        posts = Post.objects.filter(author = self)

        for i in posts:
            post_rating += i.rating

        comments = Comment.objects.filter(user = self.user)

        for c in comments:
            comments_rating += c.rating

        post_comments = Comment.objects.filter(post__author=self)

        for b in post_comments:
            post_comments_rating += b.rating

        self.rating = post_rating * 3 + comments_rating + post_comments_rating
        self.save()


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True, help_text=_('category name'))
    subscribers = models.ManyToManyField(User, null=True, blank=True, related_name='categories')

    def __str__(self):
        return self.category


class Post(models.Model):
    article = 'AR'
    news = 'NE'
    POSITIONS = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    type = models.CharField(max_length=250, choices = POSITIONS)
    time = models.DateTimeField(auto_now_add = True)
    category = models.ManyToManyField(Category, through = 'PostCategory')
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating = int(self.rating) + 1 if self.rating < 10 else + 0
        self.save()

    def dislike(self):
        self.rating = int(self.rating) - 1 if self.rating > 0 else - 0
        self.save()
    
    def preview(self):
        return f'{self.text[0:124]}...'
    
    def __str__(self):
        return f'''{self.title.title()}'''
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'post-{self.pk}')
    


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating = int(self.rating) + 1 if self.rating < 10 else + 0
        self.save()

    def dislike(self):
        self.rating = int(self.rating) - 1 if self.rating > 0 else - 0
        self.save()


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    kind = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='kinds',
        verbose_name=pgettext_lazy('help text for MyModel model', 'This is the help text'),
    )