# tests/test_valrut.py

import unittest
from rut_validator import valrut

class TestValRut(unittest.TestCase):

    def test_valid_rut(self):
        self.assertTrue(valrut("12.345.678-5"))
        self.assertTrue(valrut("12345678-5"))

    def test_invalid_rut(self):
        self.assertFalse(valrut("12.345.678-9"))
        self.assertFalse(valrut("12345678-9"))
        self.assertFalse(valrut("12.345.678-K"))
        self.assertFalse(valrut("12345678-K"))

    def test_formatting(self):
        self.assertTrue(valrut("12.345.678-5"))
        self.assertTrue(valrut("123456785"))

if __name__ == "__main__":
    unittest.main()
