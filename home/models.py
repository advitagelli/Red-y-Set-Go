from django.db import models
from django.contrib.auth.models import User
import datetime

class UserCycleData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cycle_data')
    cramp_level = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 11)], help_text="Rate your cramp level from 1 (no cramps) to 10 (severe cramps).")
    current_date = models.DateField(help_text="The selected date from the calendar.", default=datetime.date.today)
    height = models.FloatField(help_text="Enter your height in cm")
    weight = models.PositiveIntegerField(help_text="Enter your weight in pounds.")
    age = models.PositiveIntegerField(help_text="Enter your age in years.")
    previous_cycle_start = models.DateField(help_text="The selected date from the calendar.", default=datetime.date.today)
    previous_cycle_end = models.DateField(help_text="The selected date from the calendar.", default=datetime.date.today)
    predicted_cycle_length = models.PositiveIntegerField(null=True, blank=True)
    last_cycle_date = models.DateField(null=True, blank=True)
    predicted_next_cycle_start = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Cycle Data - Age: {self.age}"

    class Meta:
        verbose_name = "User Cycle Data"
        verbose_name_plural = "User Cycle Data"


