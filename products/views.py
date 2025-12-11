from django.views import generic
from .models import Category, Product

class IndexView(generic.ListView):
    model = Product

class DetailView(generic.DetailView):
    model = Product
