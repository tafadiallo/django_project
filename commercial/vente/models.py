from django.db import models

# Create your models here.
class Commande(models.Model):

    name = models.CharField(max_length=60)
    date = models.DateField()
    etat_ = models.CharField(max_length=45)
    client = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Categorie(models.Model):

    name = models.CharField(max_length=300)
    decsription = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Produit(models.Model):

    name = models.CharField(max_length=300)
    prix_vente = models.CharField(max_length=300)
    etat = models.CharField(max_length=300)
    quantite_disponible = models.LongField(max_length=300)
    decsription = models.CharField(max_length=300)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ligne(models.Model):

    quantite = models.LongField(max_length=300)
    prix_unitaire = models.LongField(max_length=300)
    prix_total = models.LongField(max_length=300)
    commande = models.ForeignKey(commande,on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return self.quantite

class User(models.Model):

    name = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name