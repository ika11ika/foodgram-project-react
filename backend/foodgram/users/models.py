from django.contrib.auth.models import AbstractUser
from django.db import models

USER = 'user'
ADMIN = 'admin'

ROLE_CHOICES = (
    (USER, 'Аутентифицированный'),
    (ADMIN, 'Администратор'),
)


class User(AbstractUser):
    login = models.CharField(
        max_length=150,
        unique=True,
        null=True,
        verbose_name='Логин'
    )
    password = models.CharField(
        max_length=150,
        verbose_name='Пароль'
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Email'
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия'
    )
    role = models.CharField(
        'Роль',
        blank=True,
        max_length=20,
        choices=ROLE_CHOICES,
        default=USER,
    )

    class Meta:
        ordering = ['login']

    @property
    def is_admin(self):
        return self.role == ADMIN

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Follow(models.Model):
    """Модель подписки на автора"""
    user = models.ForeignKey(
        User,
        related_name='user',
        verbose_name='Подписчик',
        on_delete=models.CASCADE,
    )
    following = models.ForeignKey(
        User,
        related_name='following',
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.user} - {self.following}'

    class Meta:
        ordering = ['following']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_following'
            )
        ]
