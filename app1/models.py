from django.db import models

class FanSpecification(models.Model):
    speed_level = models.IntegerField(primary_key=True)
    current = models.FloatField()

    def __str__(self):
        return f'Speed {self.speed_level} - Current {self.current}A'


class FanLog(models.Model):
    status = models.BooleanField()  # True = ON, False = OFF
    speed_level = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Status: {"ON" if self.status else "OFF"} - Speed: {self.speed_level} @ {self.timestamp}'
