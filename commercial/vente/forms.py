from django import forms
from django.forms import fields
from vente.models import Categorie, Produit


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__"


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"
