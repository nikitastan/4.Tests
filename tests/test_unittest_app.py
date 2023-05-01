from unittest import TestCase
from app import get_visits, get_unique_ids, max_stats


class Tests(TestCase):
    def test_get_visits(self):
        current_value = get_visits()
        expected_value =[{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']},
                         {'visit7': ['Тула', 'Россия']},
                         {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']},
                         {'visit10': ['Архангельск', 'Россия']}]
        self.assertEqual(current_value, expected_value)

    def test_unique_ids(self):
        current_value = get_unique_ids()
        expected_value = [98, 35, 15, 213, 54, 119]
        self.assertEqual(current_value, expected_value)

    def test_max_stats(self):
        current_value = max_stats()
        expected_value ='yandex'
        self.assertEqual(current_value, expected_value)

