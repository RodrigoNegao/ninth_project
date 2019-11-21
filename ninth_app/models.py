from django.db import models
from accounts.models import User


class ResumeUser(models.Model): #temporaryUser
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    first_name1 = models.CharField(max_length=50)
    last_name1 = models.CharField(max_length=128)
    nphone1 = models.CharField(max_length=13)
    nphone2 = models.CharField(max_length=13)
    email = models.CharField(max_length=254)
    driverslicense = models.CharField(max_length=3 )  #choices=id_drive
    address = models.CharField(max_length=254)
    neighborHood = models.CharField(max_length=128)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=9)
    maritalStatus = models.CharField(max_length=128)
    levelStudy = models.CharField(max_length=128)
    lInstitution = models.CharField(max_length=128)
    lyearFinish = models.CharField(max_length=4)
    course = models.CharField(max_length=128)
    cInstitution = models.CharField(max_length=128)
    cyearFinish = models.CharField(max_length=4)
    studyTime = models.CharField(max_length=5)
    company = models.CharField(max_length=128)
    function = models.CharField(max_length=128)
    worktime = models.CharField(max_length=128)
    functionDescribe = models.CharField(max_length=300)
