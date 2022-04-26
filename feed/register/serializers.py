from rest_framework import serializers
from feed_app.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .validators import EmailValidator, NumberValidator, LetterValidator


class RegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации нового пользователя"""
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all()), EmailValidator.validate])
    password = serializers.CharField(write_only=True, required=True, validators=[LetterValidator.validate, NumberValidator.validate])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
