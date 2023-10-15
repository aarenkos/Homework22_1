from django.urls import path

# from catalog import views
# from catalog.views import contacts, card, home

# urlpatterns = [
#     path('', home),
#     path('contacts/', contacts),
#     path('card/<int:product_id>/', card, name='product_detail')
#     # path('card/', card)
# ]

from catalog.views import ProductListView, ContactsView, CardDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('view/<int:pk>/', CardDetailView.as_view(), name='view_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]