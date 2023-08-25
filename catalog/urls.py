from django.urls import path

from catalog import views
from catalog.views import contacts, card, home

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('card/<int:product_id>/', card, name='product_detail')
    # path('card/', card)
]
