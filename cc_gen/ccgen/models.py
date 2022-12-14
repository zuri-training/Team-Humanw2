from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Design(models.Model):
    file=models.FileField(null=True, upload_to='documents/%Y/%m/%d/', help_text='select the file to upload')
    name=models.CharField(help_text="design name", max_length=20, null=True,)
    description=models.CharField(max_length=252, null=True,)

    def __str__(self):
        return self.name

class Comment(models.Model):
    comment=models.CharField(max_length=252, null=True,)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    design=models.ForeignKey(Design, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class Download(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    design=models.ForeignKey(Design, on_delete=models.CASCADE)
    DOWNLOAD_STATUS=(('d', 'Downloaded'), ('u', 'Undownload'), ('s', 'Saved'))
    downloaded=models.CharField(max_length=1, choices=DOWNLOAD_STATUS, default='u', help_text='Downloaded?')
    time_of_download=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.id)
