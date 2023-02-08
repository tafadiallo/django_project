from django.contrib import admin
from django.urls import path
from vente import views
urlpatterns = [
    #config categorie
    path('createCateg',views.createCategorie),
    path('listCateg',views.listCateg,name='show'),
    path('editCateg/<int:id>',views.editCategorie,name='edit_categ'),
    path('updateCateg/<int:id>', views.updateCategorie),
    path('deleteCateg/<int:id>', views.deleteCategorie,name='delete_categ'),
    #config produit
    path('createProd', views.createProduit),
    path('listProd', views.listProd, name='prod'),
    path('editProd/<int:id>', views.editProduit, name='edit_prod'),
    path('updateProd/<int:id>', views.updateProduit),
    path('deletProd/<int:id>', views.deleteProduit, name='delete_prod'),
    #config login
    path('admin/', admin.site.urls),
]
