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

        return super().save(*args, **kwargs)    

    def __str__(self):
        return(self.user.username)

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return(self.user.username)



"""
class Profile(models.Model):
    HSTL = (('DS','Day Scholar'), ('HSTL', 'Hostel'), ('PG', 'Paying Guest'))
    TRANS = (('SW','Self Walk'), ('SV','Self Vehicle'), ('PT','Public Transport'))
    YEAR = (('FY','First Year'),('SY','Second Year'),('TY','Third Year'),('LY','Fourth Year'))
    CLGE = (('GCEBODI','Government College of Engineering, Bodinayakkanur'),('OTHER',"Other"))
    DESG = (('STU','Student'),('STF','Staff'))
    BLOOD = (('A +ve','A +ve'), ('A -ve','A -ve'), ('B +ve','B +ve'), ('B -ve','B -ve'), ('O +ve','O +ve'), ('O -ve','O -ve'), ('AB +ve','AB +ve'), ('AB -ve','AB -ve'))
    MNTH = (('JAN','January'),('FEB','February'),('MAR','March'),('APR','April'),('MAY','May'),('JUN','June'),('JUL','July'),('AUG','August'),('SEP','September'),('OCT','October'),('NOV','November'),('DEC','December'))
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    FirstName = models.CharField(blank=True, max_length=25, help_text='First name', )
    LastName = models.CharField(blank=True, max_length=25, help_text='Last name')
    FatherName = models.CharField(blank=True, max_length=25, help_text="Father's name")
    MotherName = models.CharField(blank=True, max_length=25, help_text="Mother's name")
    BDay = models.CharField(blank=True, max_length=2, help_text="Birth Day")
    BMonth = models.CharField(max_length=15, choices=MNTH, help_text='Birth Month', default='JAN')
    BYear = models.CharField(max_length=4, help_text="Birth Year", blank=True)
    Age = models.CharField(max_length=25, blank=True, help_text='Age')
    Sex = models.CharField(max_length=10, choices=GEN, default='male', help_text='Gender')
    Address1 = models.CharField(blank=True, max_length=100, help_text='Address 1')
    Address2 = models.CharField(blank=True, max_length=100, help_text='Address 2')
    Address3 = models.CharField(blank=True, max_length=100, help_text='Address 3')
    Address4 = models.CharField(blank=True, max_length=100, help_text='Address 4')
    City = models.CharField(max_length=25, blank=True, help_text='City/Town')
    Pincode = models.CharField(blank=True, max_length=6, help_text='Pincode')
    YourPhone = models.CharField(blank=True, max_length=10, help_text='Your Phone Number')
    IsWA = models.BooleanField(default=True)
    FatherPhone = models.CharField(blank=True, max_length=10, help_text="Father's Phone Number")
    MotherPhone = models.CharField(blank=True, max_length=10, help_text="Mother's Phone Number")
    State = models.CharField(max_length=15, choices=STATE, default='TN', help_text='State/Territory')
    Country = models.CharField(max_length=30, default='India', help_text='Country')
    Aadhar =  models.CharField(blank=True, max_length=16, help_text='Aadhar Number')
    License = models.CharField(max_length=25, blank=True, help_text='License Number')
    Passport = models.CharField(max_length=25, blank=True, help_text='Passport Number')
    VoterID = models.CharField(max_length=25, blank=True, help_text='VoterID Number')
    Department = models.CharField(max_length=15, choices=DEPT, blank=True, help_text='Department')
    College = models.CharField(max_length=100, choices=CLGE, blank=True, help_text='College, City', default='GCEBODI')
    Resident = models.CharField(max_length=15, choices=HSTL, blank=True, help_text='Resident of')
    Transport = models.CharField(max_length=15, choices=TRANS, blank=True, help_text='Medium of Transport')
    Roll = models.CharField(max_length=7, blank=True, help_text='Roll Number')
    Aureg = models.CharField(max_length=12, blank=True, help_text='Anna University Number')
    Year = models.CharField(max_length=15, choices=YEAR, blank=True, help_text='Year of Study', default='FY')
    Designation = models.CharField(max_length=15, choices=DESG, blank=True, help_text='Status', default='STU')
    BloodGroup = models.CharField(max_length=6, choices=BLOOD, blank=True,help_text='Blood Group')
    def __str__(self):
        return f'{self.user.username}' 
"""