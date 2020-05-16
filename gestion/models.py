from django.db import models

class Employe(models.Model):

    matricule = models.CharField(max_length=20)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    cin = models.CharField(max_length=10)
    adresse = models.CharField(max_length=150)
    telephone = models.CharField(max_length=10)
    dateNaissance = models.DateField()
    departement = models.CharField(max_length=30)
    emploiOccupe = models.CharField(max_length=30)
    Anciennete = models.IntegerField()
    salaireBase = models.IntegerField()

    def __init__(self):
        self.__init__()


class RH(Employe):
    def __init__(self):
        super().__init__()

class Salarie(Employe):
    def __init__(self):
        super().__init__()

class Compte(models.Model):

    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __init__(self):
        self.__init__()

class BulletinPaie(models.Model):

     prime = models.IntegerField()
     p_impot = models.IntegerField()
     p_cnss = models.IntegerField()
     p_cimr = models.IntegerField()

     def __init__(self):
         self.__init__()



