import time
import os
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def get_error_element(self):
        '''получить элемент с ошибкой'''
        return self.browser.find_element_by_css_selector('.has-error')
    
    def test_cannot_add_empty_list(self):
        '''тест: нельзя добавлять пустые элементы списка'''
        # Эдит открывает домашнюю страницу и случайно пытается отправить
        # пустой элемент списка, Она нажимает enter на пустом поле ввода
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Домашняя страница обновляется, и появляется сообщение об ошибке,
        # это срабатывает
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
                '#id_text:invalid'))
        # Эдит снова пробует теперь с неким текстом для элемента, и это
        # теперь срабатывает
        self.get_item_input_box().send_keys('Купить молоко')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
                '#id_text:valid'))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Купить молоко')
        
        # Как ни странно, Эдит решает отправить второй пустой элемент списка
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Она получает аналогичное предупреждение на странице списка
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
                '#id_text:invalid'))
        # И она может его исправить, заполнив поле неким странице списка
        self.get_item_input_box().send_keys('Сделать чай')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
                '#id_text:valid'))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Купить молоко')
        self.wait_for_row_in_list_table('2: Сделать чай')
    def test_cannot_add_dublicate_items(self):
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Купить игрушку')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Купить игрушку')

        # Случайно пытается ввести повторяющийся элемент
        self.get_item_input_box().send_keys('Купить игрушку')
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Она видит полезное сообщение об ошибке
        self.wait_for(lambda: self.assertEqual(
            self.get_error_element().text,
            "You've already got this in your list"
        ))
    def test_error_messages_are_cleared_on_input(self):
        '''тест: сообщение об ошибках очищаются при вводе'''
        # Эдит начинает список и вызывает ошибку валидации:
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Banter too thick')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Banter too thick')
        
        self.get_item_input_box().send_keys('Banter too thick')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertTrue(
            self.get_error_element().is_displayed()
        ))

        # Она начинает набирать в поле ввода, чтобы очистить ошибку
        self.get_item_input_box().send_keys('a')

        # Она довольна от того, что сообщение об ошибке исчезает
        self.wait_for(lambda: self.assertFalse(
            self.get_error_element().is_displayed()
        ))
