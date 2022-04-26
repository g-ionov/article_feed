from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from register.validators import EmailValidator


class UserManager(BaseUserManager):
    """Модель, предназначенная для создания суперпользователя через терминал"""
    def create_superuser(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Email - обязательное поле.")
        if not password:
            raise ValueError("Пароль - обязательное поле.")

        user = self.model(email=email)
        user.username = 'Default_SuperUser'
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_subscriber = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """Модель пользователя"""
    is_author = models.BooleanField(verbose_name='Автор', default=False)
    is_subscriber = models.BooleanField(verbose_name='Подписчик', default=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    email = models.EmailField(verbose_name='Адрес электронной почты', unique=True, validators=[EmailValidator.validate])

    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        default="Default_User",
        null=True,
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Article(models.Model):
    """Модель статьи"""
    title = models.CharField(max_length=127, verbose_name='Статья')
    text = models.TextField(verbose_name='Контент')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    for_subscribers = models.BooleanField(verbose_name='Для подписчиков', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title']





