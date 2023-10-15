from django.shortcuts import render, get_object_or_404

from catalog.models import Product

from django.views import View
from django.views.generic import ListView, DetailView

# Create your views here.
# def home(request):
#     contex = {
#         'object_list': Product.objects.all()
#     }
#     return render(request, 'catalog/home.html', contex)
#
class ProductListView(ListView):
    model = Product


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} {email} {message}')
#     return render(request, 'catalog/contacts.html')
#

class ContactsView(View):
    template_name = 'catalog/contacts.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
        return render(request, self.template_name)


# def card(request, product_id):
#
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'catalog/card.html', {'product': product})
#
#
class CardDetailView(DetailView):
    model = Product
