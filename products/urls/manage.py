from django.urls import path
from products.views.manage import ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'products'

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
]
