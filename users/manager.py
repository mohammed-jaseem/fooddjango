from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **exstra_fields):
        user = self.model (email=email, **exstra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email, password, **exstra_fields):
        exstra_fields.setdefault("is_staff", True)
        exstra_fields.setdefault("is_superuser", True)
        exstra_fields.setdefault("is_active", True)

        if exstra_fields.get("is_staff") is not True:
            raise ValueError("superuser must have is_staff=True.")
        if exstra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must have is_superuser=True.")
        return self.create_user(email, password, **exstra_fields)