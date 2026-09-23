# Create your models here.
from django.forms import models


class Pays(models.Model):
    nom = models.CharField(max_length=200)
    tva = models.FloatField()
    tarif_electrique = models.FloatField()
    salaire_minimum = models.FloatField()


class Ville(models.Model):
    nom = models.CharField(max_length=200)
    taxe_immobiliere = models.FloatField()
    prix_m2 = models.FloatField()
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE)


class Machine(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.FloatField()
    duree_de_vie = models.FloatField()
    cout_maintenance = models.FloatField()
    superficie = models.FloatField()


class QuantiteMachine(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    nombre = models.IntegerField()


class Lieu(models.Model):
    nom = models.CharField(max_length=200)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    superficie = models.FloatField()
    quantite_machines = models.ManyToManyField(QuantiteMachine)
    consommation_electrique = models.FloatField()


class Transport(models.Model):
    nombre_palettes = models.IntegerField()
    cout = models.FloatField()
    delai = models.FloatField()
    depart = models.FloatField()
    arrivee = models.FloatField()


class Operation(models.Model):
    nom = models.CharField(max_length=200)
    operation_suivante = models.CharField(max_length=200)
    cout = models.FloatField()
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    quantite_produits = models.IntegerField()
    heures_de_travail = models.IntegerField()
    consommation_electrique = models.FloatField()


class Produit(models.Model):
    nom = models.CharField(max_length=200)
    prix_de_vente = models.FloatField()
    duree_de_vie = models.FloatField()
    nombre_par_palette = models.IntegerField()
    operations = models.models.ForeignKey(Operation)


class PrixProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    prix_achat = models.FloatField()


class Fournisseur(models.Model):
    nom = models.CharField(max_length=200)
    prix_produits = models.ManyToManyField(PrixProduit)


class QuantiteProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    nombre = models.IntegerField()


class Stock(models.Model):
    quantite_produits = models.ManyToManyField(QuantiteProduit)
    palettes_max = models.IntegerField()
