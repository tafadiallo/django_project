from django.shortcuts import render, redirect

# Create your views here.
from vente.models import Categorie, Produit
from vente.forms import CategorieForm, ProduitForm


# Categories
def createCategorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/listCateg')
            except:
                pass
    else:
        form = CategorieForm()
    return render(request, 'index.html', {'form': form})


def listCateg(request):
    categories = Categorie.objects.all()
    return render(request, 'listCateg.html', {'categories': categories})


def editCategorie(request, id):
    categorie = Categorie.objects.get(id=id)
    return render(request, 'editCateg.html', {'categorie': categorie})


def updateCategorie(request, id):
    categorie = Categorie.objects.get(id=id)
    form = CategorieForm(request.POST, instance=categorie)
    if form.is_valid():
        form.save()
        return redirect('/listCateg')
    return render(request, 'editCateg.html', {'categorie': categorie})


def deleteCategorie(request, id):
    categorie = Categorie.objects.get(id=id)
    categorie.delete()
    return redirect('/listCateg')


# Produits
def createProduit(request):
    if request.method == 'POST':
        form_prod = ProduitForm(request.POST)
        print(form_prod)
        if form_prod.is_valid():
            print('**************')
            try:
                form_prod.save()
                return redirect('/listProd')
                print('*******##############*******')
            except:
                pass
    else:
        form_prod = ProduitForm()
    return render(request, 'addProd.html', {'form_prod': form_prod})


def listProd(request):
    produits = Produit.objects.all()
    return render(request, 'listprod.html', {'produits': produits})


def editProduit(request, id):
    produit = Produit.objects.get(id=id)
    return render(request, 'editProd.html', {'produit': produit})


def updateProduit(request, id):
    produit = Produit.objects.get(id=id)
    form_prod = ProduitForm(request.POST, instance=produit)
    print('rrrrrrrrrrrrrrrrrr')
    if form_prod.is_valid():
        print('rrrrrrrr***********rrrrrrrrrr')
        form_prod.save()
        return redirect('/listProd')
    return render(request, 'editProd.html', {'produit': produit})


def deleteProduit(request, id):
    produit = Produit.objects.get(id=id)
    produit.delete()
    return redirect('/listProd')
