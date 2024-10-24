from django.db import models


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

#De forma predeterminada, todos los modelos se crearán como 
#tablas en la base db.sqlite3
