import unittest
from module_11_city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country('santiago', 'chile'), 'santiago, chile')

    def test_city_country_population(self):
        self.assertEqual(city_country('santiago', 'chile', 5_000_000), 'santiago, chile - population 5000000')


if __name__ == '__main__':
    unittest.main()