import unittest
from qcharm_gen.qr_generator.generator import QRCodeGenerator
import os


class TestQRCodeGenerator(unittest.TestCase):
    def test_generate_qr_code(self):
        data = "Test QR"
        file_path = "test_qr.png"
        QRCodeGenerator.generate(data, file_path)
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
