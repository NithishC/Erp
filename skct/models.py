from django.db import models
from django.contrib.auth.models import User

class Proof(models.Model):
    act=models.CharField(max_length=300,default="NoActivitySpecified")
    des=models.CharField(max_length=300,default="Null")
    pdf=models.FileField(upload_to='proof')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 

class Staff(models.Model):
    name=models.CharField(max_length=300)
    dept=models.CharField(max_length=300,default='')
    desig=models.CharField(max_length=300,default='')
    def __str__(self):
        return self.name


class It(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Cse(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Mech(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Eee(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Ece(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Ice(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Civil(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Sh(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Mba(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Hod(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ProfDisplay(models.Model):
    user=models.CharField(max_length=300,default="AnonymousUser")

    def __str__(self):
        return self.user

