from django.db import models

class Train(models.Model):
    train_id = models.CharField(max_length=5, primary_key=True)
    model = models.CharField(max_length=255)
    max_speed = models.PositiveIntegerField()
    no_of_seats = models.PositiveIntegerField()
    no_of_toilets = models.PositiveIntegerField()
    has_reclining_seats = models.BooleanField(default=False)
    has_folding_tables = models.BooleanField(default=False)
    has_disability_access = models.BooleanField(default=False)
    has_luggage_storage = models.BooleanField(default=False)
    has_vending_machines = models.BooleanField(default=False)
    has_food_service = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.train_id} - {self.model}"

    class Meta:
        verbose_name = "Train"
        verbose_name_plural = "Trains"


class CrewInCharge(models.Model):
    crew_id = models.CharField(max_length=4, primary_key=True)
    leader_fn = models.CharField(max_length=255)
    leader_ln = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.leader_fn} {self.leader_ln}"

    class Meta:
        verbose_name = "Crew in Charge"
        verbose_name_plural = "Crew in Charge"


class MaintenanceHistory(models.Model):
    maintenance_id = models.CharField(max_length=4, primary_key=True)
    task = models.CharField(max_length=255)
    condition = models.CharField(max_length=20, choices=[
        ('Excellent', 'Excellent'),
        ('Very Good', 'Very Good'),
        ('Good', 'Good'),
        ('Bad', 'Bad'),
        ('Very Bad', 'Very Bad'),
        ('Unsatisfactory', 'Unsatisfactory')
    ])
    date_maintained = models.DateField()
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    crew = models.ForeignKey(CrewInCharge, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.maintenance_id} - {self.task}"

    class Meta:
        verbose_name = "Maintenance History"
        verbose_name_plural = "Maintenance History"