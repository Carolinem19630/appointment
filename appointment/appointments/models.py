from django.db import models

# Create your models here.

class Appointment(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}: {self.start} - {self.end} at {self.location}"

class Attendee(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    appointments = models.ManyToManyField(Appointment, blank=True, related_name="attendees")

    def __str__(self):
        return f"{self.first} {self.last}"
