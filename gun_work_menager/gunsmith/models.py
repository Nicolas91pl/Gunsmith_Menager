from django.db import models

class Licences(models.Model):
    id = models.BigAutoField(primary_key=True)
    serial_number = models.CharField(max_length=60, unique=True)

    conc = 'conc'
    sport = 'sprt'
    coll = 'coll'
    self_def = 'self'
    hunt = 'hunt'
    Licences_Type_Choices = [
        (conc, 'Koncesja'),
        (sport, 'Sport'),
        (coll, 'Kolekcjonerska'),
        (self_def, 'Ochrona Osobista'),
        (hunt, 'Myśliwska')
    ]
    type = models.CharField(max_lenght=4, choices=Licences_Type_Choices, blank=False)
    realise_date = models.DateField()
    authority = models.CharField(max_length=120)

