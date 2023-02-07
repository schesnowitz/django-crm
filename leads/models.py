from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # add to settings AUTH_USER_MODEL = 'leads.User'
    pass
    def __str__(self):
        return self.email

class Lead(models.Model):
    # CHOICE_SOURCE = (
    #     ('YouTube', 'YouTube'),
    #     ('Google', 'Google'),
    #     ('Facebook', 'Facebook'),
    #     ('Twitter', 'Twitter'),
    #     )
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    age             = models.IntegerField(default=0)
    agent           = models.ForeignKey("Agent", on_delete=models.CASCADE)
    # phoned          = models.BooleanField(default=False)
    # source          = models.CharField(choices=CHOICE_SOURCE, max_length=50)
    # profile_picture = models.ImageField(blank=True, null=True, upload_to=None, height_field=None, 
    #                                             width_field=None, max_length=None)
    # special_files   = models.FileField(blank=True, null=True, upload_to=None, max_length=100)                                                
    def __str__(self):
         return (f"{self.first_name} {self.last_name}")


class Agent(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.email


