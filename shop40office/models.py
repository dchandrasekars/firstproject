from django.db import models

# Create your models here.
class EmployeeMaster(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    desig=models.CharField(max_length=100)
    
    



    def __str__(self):
        return self.name

   