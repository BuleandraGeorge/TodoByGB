from django.test import TestCase
from .models import Item


class TestViews(TestCase):

    def test_view_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Todo/todo_list.html')

    def test_view_edit_task(self):
        item = Item.objects.create(name="Todo task test")
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Todo/edit_task.html')

    def test_view_add_task(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Todo/add_task.html')

    def test_can_add_task(self):
        response = self.client.post('/add/', name='test add item')
        self.assertRedirects(response, '/')


    def test_can_toggle_task(self):
        item = Item.objects.create(done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_delete_task(self):
        item = Item.objects.create(name="To be deleted")
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)