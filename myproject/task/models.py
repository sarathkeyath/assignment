from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name

class Employee(models.Model):
    employee_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    Company_namee = models.CharField(max_length=100)
    salary = models.FloatField()
    manager_id = models.IntegerField()
    department_id = models.IntegerField()
    fkey = models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name




