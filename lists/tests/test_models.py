from lists.models import Item, List
from django.test import TestCase
from django.core.exceptions import ValidationError

class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'Первый элемент списка'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Элемент второй'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'Первый элемент списка')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Элемент второй')
        self.assertEqual(second_saved_item.list, list_)
    def test_cannot_save_empty_list(self):
        '''тест: нельзя добавлять пустые элементы списка'''
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.full_clean()
            item.save()
    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')

    def test_CAN_save_same_item_to_different_lists(self):
        '''тест: Может сохранить тот же элемент в разные списки'''
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='bla')
        item = Item.objects.create(list=list2, text='bla')
        item.full_clean()
    def test_list_ordering(self):
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='i1')
        item2 = Item.objects.create(list=list1, text='item 2')
        item3 = Item.objects.create(list=list1, text='3')
        self.assertEqual(
            list(Item.objects.all()),
            [item1, item2, item3]
        )
    def test_string_representation(self):
        item = Item(text='some text')
        self.assertEqual(str(item), 'some text')