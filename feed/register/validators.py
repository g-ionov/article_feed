import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class NumberValidator(object):
    """Проверка наличия цифры в пароле"""
    def validate(self, *args, user=None):
        password = self
        """Проверка на наличие аргументов происходит из-за того, что 
        создание пользователя через админку принимает 3 аргумента, а через эндпоинт - 2"""
        if args:
            password = str(args)
        if not re.findall('\d', password):
            raise ValidationError(_("Пароль должен содержать хотя бы одну цифру."), code='password_no_number')

    def get_help_text(self):
        return _("Пароль должен содержать хотя бы одну цифру")


class LetterValidator(object):
    """Проверка наличия буквы любого регистра в пароле"""
    def validate(self, *args, user=None):
        password = self
        """Проверка на наличие аргументов происходит из-за того, что 
        создание пользователя через админку принимает 3 аргумента, а через эндпоинт - 2"""
        if args:
            password = str(args)
        if not re.findall('[a-z]', password) and not re.findall('[A-Z]', password):
            raise ValidationError(_("Пароль должен содержать хотя бы одну букву любого регистра"), code='password_no_letter')

    def get_help_text(self):
        return _("Пароль должен содержать хотя бы одну букву любого регистра")

class EmailValidator(object):
    """Валидация почты"""
    def validate(self, *args, user=None):
        email = self
        """Проверка на наличие аргументов происходит из-за того, что 
        создание пользователя через админку принимает 3 аргумента, а через эндпоинт - 2"""
        if args:
            email = str(args)
        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            raise ValidationError("Email должен соответствовать следующей маске: email@email.com")
        else:
            return object
    #
    # def get_help_text(self):
    #     return _("Email должен соответствовать следующей маске: email@email.com")

