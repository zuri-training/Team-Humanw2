from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Download(models.Model):
    user-id=models.ForeignKey(User, on_delete=models.CASCADE)
    design-id=models.ForeignKey(Design, on_delete=models.CASCADE)
    downloaded=models.BooleanField(null=True)

class Design(models.Model):
    file=models.FileField(null=True, help_text='select the file to upload')
    name=models.CharField(help_text="design name", max_length=20, null=True,)
    description=models.CharField(max_length=252, null=True,)


class Comment(models.Model):
    comment=models.CharField(max_length=252, null=True,)
    user-id=models.ForeignKey(User, on_delete=models.CASCADE)
    design-id=models.ForeignKey(Design, on_delete=models.CASCADE)
