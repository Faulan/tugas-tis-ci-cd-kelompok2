# test_app.py
import unittest
from app import tambah, kurang

class TestKalkulator(unittest.TestCase):

    def test_tambah(self):
        # Menguji apakah 2 + 3 hasilnya benar 5
        self.assertEqual(tambah(2, 3), 5)

    def test_kurang(self):
        # Menguji apakah 5 - 2 hasilnya benar 3
        self.assertEqual(kurang(5, 2), 3)

if __name__ == '__main__':
    # Menjalankan test dan menyimpan output ke file teks (untuk laporan)
    with open('test-report.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner)