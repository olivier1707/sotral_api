from django.db import models


# Create your models here.
class Bus(models.Model):
    idbus = models.IntegerField()
    nomconducteur = models.CharField(max_length=100)

    def __str__(self):
        return f"BUS : {self.idbus} et {self.nomconducteur}"


class Ligne(models.Model):
    idligne = models.IntegerField()
    codeLigne = models.CharField(max_length=50)
    libelleLigne = models.CharField(max_length=50)
    Bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='ligne')


class Section(models.Model):
    idsection = models.IntegerField()
    codeSection = models.CharField(max_length=50)
    libelleSection = models.CharField(max_length=50)
    Ligne = models.ForeignKey(Ligne, on_delete=models.CASCADE, related_name='section')


class Tarif(models.Model):
    idtarif = models.IntegerField()
    codeTarif = models.CharField(max_length=50)
    prix = models.IntegerField()


class Utilisateur(models.Model):
    idUser = models.IntegerField()
    codeUser = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    compte = models.IntegerField()


class Voyager(models.Model):
    idvoyage = models.IntegerField()
    codeVoyage = models.CharField(max_length=50)
    valide = models.BooleanField(default=0)
    Utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='voyage')



