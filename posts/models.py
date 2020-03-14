from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

CATEGORY_CHOICES = (
    ('Dj', 'Django'),
    ('R', "Ruby")
)


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    custom_id = models.IntegerField(default=None)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=None)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
