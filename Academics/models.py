from django.db import models
from django.contrib.auth.models import User

from skct.models import Staff
# Create your models here.

class Academics(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='Academics')
    points=models.IntegerField(default=0)
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 
    


class Feedback(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='Feedback')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class Innovation(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf = models.FileField(upload_to='Innovations')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class UG(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='UG')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class PG(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='PG')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class ExtraCurricular(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='Extracurricular')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 



class AllClear(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='Allclear')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class ThreeClear(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='ThreeClear')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class Article(models.Model):
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='Article')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class Competitive(models.Model):
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='Competitive')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class Startups(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='Startups')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class Awards(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='Awards')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class Prizes(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='Prizes')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class Internship(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='Internship')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class OnlineCertification(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='OnlineCertification')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 
