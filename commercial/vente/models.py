from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

class Commande(models.Model):

    name = models.CharField(max_length=60)
    date = models.DateField()
    etat = models.CharField(max_length=45)
    client = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Categorie(models.Model):

    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Produit(models.Model):

    name = models.CharField(max_length=300)
    prix_vente = models.CharField(max_length=300)
    etat = models.CharField(max_length=300)
    quantite_disponible = models.DecimalField(max_digits=5, decimal_places=2)
    decsription = models.CharField(max_length=300)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ligne(models.Model):

    quantite = models.DecimalField(max_digits=5, decimal_places=2)
    prix_unitaire = models.DecimalField(max_digits=5, decimal_places=2)
    prix_total = models.DecimalField(max_digits=5, decimal_places=2)
    commande = models.ForeignKey(Commande,on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return self.quantite
