from django.test import TestCase
from .models import Item


class TestModel(TestCase):
    def test_done_false_by_default(self):
        item = Item.objects.create(name='Todo item test')
        self.assertFalse(item.done)
