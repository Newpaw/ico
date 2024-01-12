import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from companycz.json_parser import parse_company_data
from companycz.models import Company

class TestJsonParser(unittest.TestCase):

    def test_parse_company_data(self):
        sample_data = {
            'ico': '12345678',
            'obchodniJmeno': 'Test Company',
            'primarniZdroj': 'Test Source',
        }
        company = parse_company_data(sample_data)
        self.assertIsInstance(company, Company)
        self.assertEqual(company.ico, '12345678')


    def test_parse_company_data_with_missing_data(self):
        sample_data = {
            # 'ico': '12345678', # Tento klíč chybí
            'obchodniJmeno': 'Test Company'
        }
        company = parse_company_data(sample_data)
        self.assertIsNone(company.ico) 
        self.assertEqual(company.obchodniJmeno, 'Test Company')


    def test_parse_company_data_with_invalid_input(self):
        with self.assertRaises(ValueError):
            sample_data = None  # neplatný vstup
            parse_company_data(sample_data)

        with self.assertRaises(ValueError):
            sample_data = "some string"  # další neplatný vstup
            parse_company_data(sample_data)

if __name__ == '__main__':
    unittest.main()