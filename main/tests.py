from django.test import TestCase, Client
from main.models import Item

class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Item.objects.create(
            name='Porsche 918 Spyder',
            amount=7,
            price=1144000,
            category='Sports Car',
            description='holy trinity supremacy'
        )

    def test_name_max_length(self):
        item = Item.objects.get(id=1)
        max_length = item._meta.get_field('name').max_length
        self.assertLessEqual(len(item.name), max_length)

    def test_amount_data_type(self):
        item = Item.objects.get(id=1)
        self.assertIsInstance(item.amount, int)

    def test_price_data_type(self):
        item = Item.objects.get(id=1)
        self.assertIsInstance(item.price, int)

    def test_category_max_length(self):
        item = Item.objects.get(id=1)
        max_length = item._meta.get_field('category').max_length
        self.assertLessEqual(len(item.category), max_length)

    def test_description_max_length(self):
        item = Item.objects.get(id=1)
        self.assertIsInstance(item.description, str)


#
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')