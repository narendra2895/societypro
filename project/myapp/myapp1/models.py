from django.db import models
from django.core.exceptions import ValidationError
import datetime

def check_space(value):
    if value == " ":
        raise ValidationError("The field cannot be empty")

# Create your models here.
class record_model(models.Model):
    cname= models.CharField(max_length=50, validators=[check_space])
    cemail= models.CharField(max_length=50, validators=[check_space])
    cphone= models.CharField(max_length=50, validators=[check_space])
    cservice= models.CharField(max_length=50, validators=[check_space])
    cmessage= models.TextField(validators=[check_space])
    
    def __str__(self):
        return self.cname

class service_info(models.Model):
    sname= models.CharField(max_length=50)
    sdesc= models.CharField(max_length=150)
    sdetails=models.TextField()
# and ru your queries python manage.py makemigrations-------->python manage.py migrate

    def __str__(self):
        return self.sname
    


class blog_model(models.Model):
    btitle= models.CharField(max_length=50, validators=[check_space])
    bcontent= models.TextField(validators=[check_space])
    bdate=models.DateField(default=datetime.date.today)
# and ru your queries python manage.py makemigrations-------->python manage.py migrate

    def __str__(self):
        return self.btitle