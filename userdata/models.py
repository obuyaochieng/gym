from django.db import models

# Create your models here.
# userdata/models.py these for logins
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    useremail = models.EmailField(max_length=255)

    def __str__(self):
        return self.username

