import time
import os
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list(self):
        '''тест: нельзя добавлять пустые элементы списка'''
        # Эдит открывает домашнюю страницу и случайно пытается отправить
        # пустой элемент списка, Она нажимает enter на пустом поле ввода

        # Домашняя страница обновляется, и появляется сообщение об ошибке,
        # это срабатывает

        # Как ни странно, Эдит решает отправить второй пустой элемент списка

        # Она получает аналогичное предупреждение на странице списка

        # И она может его исправить, заполнив поле неким странице списка
        self.fail('напиши меня!')