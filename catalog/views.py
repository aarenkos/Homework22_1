from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.
def home(request):
    contex = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', contex)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} {email} {message}')
    return render(request, 'catalog/contacts.html')

def card(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/card.html', {'product': product})


