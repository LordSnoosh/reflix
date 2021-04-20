from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}/{self.email}'

    # def validate(self, value):
    #     super().validate(value)
    #     for email in value:
    #         validate_email(email)