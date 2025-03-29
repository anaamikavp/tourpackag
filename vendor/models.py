from django.db import models

from user.models import register_table


# Create your models here.
class package_table(models.Model):
    #id will be created automatically
    package_name=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    duration=models.CharField(max_length=50)
    price=models.FloatField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    description=models.CharField( max_length=150)
    start_date=models.DateField()
    end_date=models.DateField()
    images=models.FileField()
    status=models.CharField(max_length=20)
    vendor_id=models.ForeignKey(register_table,on_delete=models.SET_DEFAULT,default=1)


    class Meta:
        db_table="packages"