from django.db import models

# Create your models here.

class InsureType(models.Model):
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "insure_type"

    def __str__(self):
        return "%s" % (self.name)



class CarType(models.Model):
    name = models.CharField(max_length=20 )
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "car_type"

    def __str__(self):
        return "%s" % (self.name)

class Agent(models.Model):
    code = models.CharField(max_length=20 )
    first_name = models.CharField(max_length=200 )
    last_name = models.CharField(max_length=200 )
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "agent"

    def __str__(self):
        return "%s(%s %s)" %(self.code, self.first_name, self.last_name)
class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=10)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "customer"
    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)

class Service(models.Model):
    insure_type = models.ForeignKey(InsureType, on_delete=models.CASCADE)
    customer  = models.ForeignKey(Customer, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=7)
    remark = models.TextField(null=True, default=None)

    class Meta:
        db_table = "service"
    def __str__(self):
        return "%s - %s" %(self.customer, self.agent)