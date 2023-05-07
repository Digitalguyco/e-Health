from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, first_name, password, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            password=password,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, first_name, password, **extra_fields)

    def create_superuser(self, email, first_name, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, first_name,  password, **extra_fields)