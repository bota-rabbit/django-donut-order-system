from django.views import generic
from products.models import Category, Product

class ProductListView(generic.ListView):
    model = Product

class ProductDetailView(generic.DetailView):
    model = Product
