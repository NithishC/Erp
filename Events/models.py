from django.db import models

# Create your models here.


class Grant(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='upload')
    points=models.IntegerField(default=0)
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class InternationalConf(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='upload')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class NationalConf(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf = models.FileField(upload_to='upload')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class Workshop(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='upload')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class FDP(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='upload')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class InterCollege(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='upload')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class InternationalConf2(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='upload')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class NationalConf2(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf = models.FileField(upload_to='upload')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class Workshop2(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='upload')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class FDP2(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='upload')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class InterCollege2(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='upload')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 

