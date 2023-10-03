from django.db import models


from django.contrib.auth.models import User






class Files(models.Model):
    file = models.FileField(upload_to='user_files/', null=True, blank=True)  
    logo = models.ImageField(upload_to='user_logos/', null=True, blank=True)
    
    
    
class Information_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    participant = models.CharField(max_length=200)
    address1 = models.TextField()
    address2 = models.TextField(null=True, blank=True)
    tel = models.TextField()
    mob = models.TextField(null=True, blank=True)
    mail = models.TextField(null=True, blank=True)
    exhibition = models.TextField(null=True, blank=True)
    contact_person = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    payed = models.FloatField(null=True, blank=True)
    status = models.BooleanField(default=False, null=True)
    employer = models.TextField(null=True,blank=True)
    date = models.TimeField(auto_now_add=True,)
    file = models.ForeignKey(Files, on_delete=models.CASCADE)
      