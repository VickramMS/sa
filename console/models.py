from django.db import models
from django.contrib.auth.models import User



class Subject(models.Model):
    CRED = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'))
    SEM = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'))
    subname = models.CharField(max_length=100)
    subcode = models.CharField(max_length=7)
    subcred = models.CharField(max_length=1, choices=CRED, default='1')
    sem = models.CharField(max_length=1, choices=SEM, default='1')

    def __str__(self):
        return self.subname

class Internal(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks1 = models.IntegerField(default=0)
    marks2 = models.IntegerField(default=0)
    marks3 = models.IntegerField(default=0)
    marks = models.IntegerField(default=100)
    marksob = models.IntegerField(default=0)

    def save(self):
        self.marksob = (self.marks1 + self.marks2 + self.marks3)/15
        return super(Internal, self).save()


    def __str__(self):
        return f'{self.student.profile.Aureg}-SEM.{self.subject.sem}'


class Semester(models.Model):    
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marksob = models.IntegerField(default=0)
    markstot = models.IntegerField(default=100)

    def __str__(self):
        return f'{self.student.profile.Aureg}-{self.subject.subcode}' 



        