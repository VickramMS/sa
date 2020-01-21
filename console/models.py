from django.db import models
from django.contrib.auth.models import User



class Subject(models.Model):
    CRED = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'))
    SEM = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'))
    subname = models.CharField(max_length=100)
    subcode = models.CharField(max_length=7, unique=True)
    subcred = models.CharField(max_length=1, choices=CRED, default='1')
    sem = models.CharField(max_length=1, choices=SEM, default='1')

    def __str__(self):
        return self.subname

class Internal(models.Model):
    DEPT = (('MECH','Mechanical'), ('CIVIL','Civil'), ('EEE','Electrical and Electronics'), ('ECE','Electronics and Communication'), ('CSE','Computer Science and Engineering'),('OTHER','Others'))
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    dept = models.CharField(max_length=5, choices=DEPT, default='MECH')
    marks1 = models.IntegerField(default=0)
    marks2 = models.IntegerField(default=0)
    marks3 = models.IntegerField(default=0)
    marks = models.IntegerField(default=100)
    marksob = models.IntegerField(default=0)

    def save(self):
        self.marksob = (self.marks1 + self.marks2 + self.marks3)/15
        return super(Internal, self).save()


    def __str__(self):
        return f'{self.student}-SEM.{self.subject.sem}'


class Grade(models.Model):
    points = models.IntegerField()
    letter = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.letter


class Semester(models.Model):  
    RESULT = (('PASS','PASS'),('RA','Reappearance is Required'),('W','Withdrawal'),('SE','Sports Exemption'),('*Ab','Absent for Univeristy Exam'))  
    DEPT = (('MECH','Mechanical'), ('CIVIL','Civil'), ('EEE','Electrical and Electronics'), ('ECE','Electronics and Communication'), ('CSE','Computer Science and Engineering'),('OTHER','Others'))
    student = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    grade = models.ForeignKey(Grade, on_delete=models.DO_NOTHING, default=1)
    dept = models.CharField(max_length=5, choices=DEPT, default='MECH')
    result = models.CharField(max_length=30, choices=RESULT, default='PASS')
    def __str__(self):
        return f'{self.student}-{self.subject.subcode}' 

class IntAssign(models.Model):
    DEPT = (('MECH','Mechanical'), ('CIVIL','Civil'), ('EEE','Electrical and Electronics'), ('ECE','Electronics and Communication'), ('CSE','Computer Science and Engineering'),('OTHER','Others'))
    staff = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    department = models.CharField(max_length=5, choices=DEPT, default='MECH')
    def __str__(self):
        return f'{self.staff}-{self.subject.subcode}'

class SemAssign(models.Model):
    DEPT = (('MECH','Mechanical'), ('CIVIL','Civil'), ('EEE','Electrical and Electronics'), ('ECE','Electronics and Communication'), ('CSE','Computer Science and Engineering'),('OTHER','Others'))   
    staff = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    semester = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, default=1)
    department = models.CharField(max_length=5, choices=DEPT, default='MECH')
    def __str__(self):
        return f'{self.staff.username}'

