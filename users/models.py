from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from . import choices as c

class User(AbstractUser):
    user_type = models.CharField(max_length=20, choices=c.USER_TYPE)
    department = models.CharField(max_length=20, choices=c.DEPT)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True)
    age = models.IntegerField(blank=True)
    

    def save(self, *args, **kwargs):
        #date calculator
        today = date.today()
        born = self.date_of_birth
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        #save 
        self.age = age
        return super().save(*args, **kwargs)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.CharField(max_length=30, choices=c.YEAR)
    roll_no = models.CharField(max_length=7, blank=True)
    reg_no = models.CharField(max_length=12, blank=True)
    avatar = models.ImageField(default='default.jpg', upload_to='media')
    father = models.CharField(max_length=50, blank=True)
    mother = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=12, choices=c.GENDER, default='MALE')
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    address3 = models.CharField(max_length=50, blank=True)
    address4 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=30, choices=c.STATE, default='TN')
    pincode = models.CharField(max_length=6, blank=True)
    full_address = models.TextField(blank=True)
    phone = models.CharField(max_length=10, blank=True)
    father_mobile = models.CharField(max_length=10, blank=True)
    mother_mobile = models.CharField(max_length=10, blank=True)
    resident = models.CharField(max_length=20, choices=c.RES, default='Hostel')
    transport = models.CharField(max_length=20, choices=c.TRANS, default='Self Walk')
    blood = models.CharField(max_length=10, choices=c.BLOOD, default='A +ve')
    aadhar = models.CharField(max_length=12, unique=True, null=True)
    
    def save(self, *args, **kwargs):
        #year calculator
        today = date.today()
        start = self.user.date_joined
        num = today.year - start.year - ((today.month, today.day) < (start.month, start.day))
        print(num)
        #save
        if num == 0:
            self.year = 'First Year'
        elif num == 1:
            self.year = 'Second Year'
        elif num == 2:
            self.year = 'Third Year'
        elif num == 3:
            self.year = 'Fourth Year'
        else:
            self.year = 'Completed'

        #address
        self.full_address = self.address1 + '\n' + self.address2 + '\n' + self.address3 + '\n' + self.address4 + '\n' + self.city + ' - ' + self.pincode


        return super().save(*args, **kwargs)    

    def __str__(self):
        return(self.user.username)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return(self.user.username)

