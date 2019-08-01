from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    fatherName = models.CharField(max_length=200)
    phoneNumber = models.BigIntegerField()
    password = models.CharField(max_length=200)
    nationalId = models.BigIntegerField()
    birthday = models.DateField(default='2000-11-11')
    male = models.BooleanField(default=False)
    region = models.CharField(max_length=200, default='Iran')


class LoanInfo(models.Model):
    Code = models.BigIntegerField()
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=10)
    intrest = models.BigIntegerField()
    maxInstallment = models.BigIntegerField()
    minInstallment = models.BigIntegerField()
    lowestAmount = models.BigIntegerField()
    highestAmount = models.BigIntegerField()


class Loan(LoanInfo):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="null")
