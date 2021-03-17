from django.db import models
from django.contrib.auth.models import User

from skct.models import Staff
# Create your models here.

class SCI(models.Model):
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


class ESCI(models.Model):
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


class RIP(models.Model):
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


class RNP(models.Model):
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


class ISBN(models.Model):
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


class IEEE(models.Model):
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


class  Guideship (models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='StudentActivities')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class  GuideshipPursuing(models.Model):
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


class Patents(models.Model):
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


class Applied(models.Model):
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


class Received(models.Model):
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


class Consultancy(models.Model):
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


class DCM(models.Model):
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


class SubjectExpert(models.Model):
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


class WOS(models.Model):
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



