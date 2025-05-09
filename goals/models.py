from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='goals')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    PRIORITY_CHOICES = [
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ]

    priority = models.CharField(
            max_length=10,
            choices=PRIORITY_CHOICES,
            default='low',
            )

    def __str__(self):
        return self.title
