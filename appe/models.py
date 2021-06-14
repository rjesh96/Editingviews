from django.db import models

# Create your models here.
class EditingView(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    salary=models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    contactno=models.IntegerField()
    email=models.EmailField()
    doj=models.DateField(auto_now=True)
