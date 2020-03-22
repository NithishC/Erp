from django.db import models

# Create your models here.

class CollegeContrib(models.Model):
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


class DepartmentContrib(models.Model):
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


class IndexedJournal(models.Model):
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
