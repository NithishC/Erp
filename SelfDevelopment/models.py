from django.db import models
from django.contrib.auth.models import User




class FacultyAttendance(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='FacultyAttendance')
    points=models.IntegerField(default=0)
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class GuestLecture(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='GuestLecture')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class GuestLectureIndustry(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf = models.FileField(upload_to='GuestLectureIndustry')
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


class PatentFiled(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='PatentFiled')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class PatentPublished(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='PatentPublished')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class PatentGranted(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='PatentGranted')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class PlacementArranged(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='PlacementArranged')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class Events(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='Events')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class MOU(models.Model):
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='MOU')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class Excellence(models.Model):
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='Excellence')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class EventsParticipation(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='EventsParticipation')
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
    pdf=models.FileField(upload_to='SelfDevelopmentAwards')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 


class OnlineCourse(models.Model):
    dept = models.CharField(default="Null",max_length=5)
    des=models.TextField(max_length=300)
    pdf=models.FileField(upload_to='OnlineCourse')
    points=models.IntegerField(default='0')
    pointsaward=models.IntegerField(default='0')
    user=models.CharField(max_length=300,default="AnonymousUser")
    def __str__(self):
        return self.user
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs) 



