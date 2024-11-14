from django.db import models

# Create your models here.
class NewMembers(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    phone=models.IntegerField(null=True)


class Meta:
    db_table='member'
    
def __str__(self):
    return f"{self.ename}"
