from django.views import generic
from products.models import Category, Product

class ProductCreateView(generic.edit.CreateView):
    model = Product
    fields = ['__all__']    

class ProductUpdateView(generic.edit.UpdateView):
    model = Product
    fields = ['__all__']    

class ProductDeleteView(generic.edit.DeleteView):
    model = Product
    