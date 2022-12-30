from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    loction = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=50,choices=(('IT','IT'),
                                                   ('Non IT','Non IT')
                                                   ))
    added_date = models.DateTimeField(auto_now=True)
    active_models = models.BooleanField(default=True)

    def __str__(self):
        return self.name
# Create Employee Model

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    type=models.CharField(max_length=50,choices=(('Manager','Manager'),
                                                 ('Soft Developer','Software Developer'),
                                                 ('Project Leader','Project Leader')))
    about = models.TextField()


    company=models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self):
        return self.name