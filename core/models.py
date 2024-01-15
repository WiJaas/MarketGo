from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_groups',
        related_query_name='customer_group',
        blank=True,
        verbose_name='groups',
        help_text='The groups this customer belongs to. A customer will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_permissions',
        related_query_name='customer_permission',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this customer.',
    )

    def __str__(self):
        return self.username
