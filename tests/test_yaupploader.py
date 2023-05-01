import unittest
from unittest import TestCase
from yaupploader import YaUploader

ya = YaUploader(token=input('Введите токен от Я.Диска: '))

class Tests(TestCase):
    def test_create_folder(self):
        resp_code = 201
        res = ya.create_folder()
        self.assertEqual(res, resp_code)


    def test_check_folder(self):
        resp_code = 200
        res = ya.check_folder()
        self.assertEqual(res, resp_code)


    @unittest.expectedFailure
    def test_is_folder_exist(self):
        resp_code = 201
        res = ya.create_folder()
        self.assertEqual(res, resp_code, 'Папка уже существует. Status=409')


    @unittest.expectedFailure
    def test_invalid_data(self):
        resp_code = 201
        res = ya.failure_function()
        self.assertEqual(res, resp_code, 'Некорректная ссылка. Status=400')

