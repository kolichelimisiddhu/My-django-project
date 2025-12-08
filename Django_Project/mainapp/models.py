from django.db import models
from django.contrib.auth.models import User

class Busdetail(models.Model):
    bus_name = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=100)
    total_seats = models.IntegerField()

    def __str__(self):
        return self.bus_name
    
class Busroutes(models.Model):
    bus=models.ForeignKey(Busdetail,on_delete=models.CASCADE)
    bus_source=models.CharField(max_length=20)
    bus_destination=models.CharField(max_length=20)
    bus_date=models.DateField()
    bus_start_time=models.TimeField()
    bus_arrival_time=models.TimeField()
    bus_ticket_price=models.IntegerField()


    def __str__(self):
        return f"{self.bus_source} to {self.bus_destination} ({self.bus_date})" 

class Busbooking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    route=models.ForeignKey(Busroutes,on_delete=models.CASCADE)
    seats=models.CharField(max_length=200)
    booked_on=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} booked {self.seats}"