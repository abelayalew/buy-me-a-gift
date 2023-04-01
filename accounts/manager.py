from django.contrib.auth.models import BaseUserManager


class AccountManger(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have email")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email,
            password=password,
            username=username,
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save(using=self._db)
        return user
