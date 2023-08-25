from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        categories_list = [
            {'name': 'TV', 'description': 'Различные Телевизоры, Проекторы, Экраны'},
            {'name': 'Phone', 'description': 'Телефоны, Смартфоны,Радиотелефоны'},
            {'name': 'Audio', 'description': 'Колонки, Наушники, Саундбары'},
        ]
        categories_for_create = []

        for category_item in categories_list:
            categories_for_create.append(Category(**category_item))

        Category.objects.bulk_create(categories_for_create)

        product_list = [{"name": "SULSUMG", "description": "Идеальное изображение",
                         "category": Category.objects.get(name="TV"),
                         "price_for_purchase": 15000, "creation_date": "2023-06-01",
                         "last_change_date": "2023-08-01"},
                        {"name": "Telefone1", "description": "Самый надежный телефон",
                         "category": Category.objects.get(name="Phone"),
                         "price_for_purchase": 5000, "creation_date": "2023-05-01",
                         "last_change_date": "2023-08-01"},
                        {"name": "Headphones777", "description": "Громкий звук",
                         "category": Category.objects.get(name="Audio"),
                         "price_for_purchase": 7000, "creation_date": "2023-06-01",
                         "last_change_date": "2023-08-01"},
                        {"name": "BS", "description": "Нормально показывает",
                         "category": Category.objects.get(name="TV"),
                         "price_for_purchase": 27000, "creation_date": "2023-06-01",
                         "last_change_date": "2023-08-01"},
                        {"name": "Telefone777", "description": "Самый тяжелый телефон",
                         "category": Category.objects.get(name="Phone"),
                         "price_for_purchase": 8000, "creation_date": "2023-05-01",
                         "last_change_date": "2023-08-01"},
                        {"name": "Headphones01", "description": "Звук есть",
                         "category": Category.objects.get(name="Audio"),
                         "price_for_purchase": 1000, "creation_date": "2023-06-01",
                         "last_change_date": "2023-08-01"},
                        ]

        products_to_create = []

        for product_item in product_list:
            products_to_create.append(Product(**product_item))

        Product.objects.bulk_create(products_to_create)

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена новыми данными.'))
