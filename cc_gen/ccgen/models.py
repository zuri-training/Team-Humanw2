from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Design(models.Model):
    file=models.FileField(null=True, upload_to='documents/%Y/%m/%d/', help_text='select the file to upload')
    name=models.CharField(help_text="design name", max_length=20, null=True,)
    description=models.CharField(max_length=252, null=True,)


class Comment(models.Model):
    comment=models.CharField(max_length=252, null=True,)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    design_id=models.ForeignKey(Design, on_delete=models.CASCADE)

class Download(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    design_id=models.ForeignKey(Design, on_delete=models.CASCADE)
    downloaded=models.BooleanField(null=True)
