from django.db import models
from users.models import User
from users import choices as c



class Subject(models.Model):
    subname = models.CharField(max_length=100)
    subcode = models.CharField(max_length=7, unique=True)
    subcred = models.CharField(max_length=2, choices=c.CRED, default='1')
    sem = models.CharField(max_length=1, choices=c.SEM, default='1')

    def __str__(self):
        return self.subname

class Internal(models.Model):
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    dept = models.CharField(max_length=5, choices=c.DEPT, default='MECH')
    marks1 = models.IntegerField(default=0, blank=True)
    marks2 = models.IntegerField(default=0, blank=True)
    marks3 = models.IntegerField(default=0, blank=True)
    marks = models.IntegerField(default=100, blank=True)
    marksob = models.IntegerField(default=0, blank=True)

    def save(self):
        self.marksob = (int(self.marks1) + int(self.marks2) + int(self.marks3)) / 15
        self.dept = self.student.department
        return super(Internal, self).save()
        
    def __str__(self):
        return f'{self.student}-SEM.{self.subject.sem}'


class Grade(models.Model):
    points = models.IntegerField()
    letter = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.letter


class Semester(models.Model):  
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING, default=1)
    dept = models.CharField(max_length=5, choices=c.DEPT, default='MECH')
    result = models.CharField(max_length=30, choices=c.RESULT, default='PASS')
    def __str__(self):
        return f'{self.student}-{self.subject.subcode}' 

class IntAssign(models.Model):
    staff = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    department = models.CharField(max_length=5, choices=c.DEPT, default='MECH')


    def __str__(self):
        return f'{self.staff}-{self.subject.subcode}'

class SemAssign(models.Model):
    staff = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, default=1)
    department = models.CharField(max_length=5, choices=c.DEPT, default='MECH')
    def __str__(self):
        return f'{self.staff.username}'

