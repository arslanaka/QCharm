import qrcode
from PIL import Image


class QRCodeGenerator:
    @staticmethod
    def generate(data, style):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        if style == "Style 1":
            img = QRCodeGenerator.apply_style_1(img)
        elif style == "Style 2":
            img = QRCodeGenerator.apply_style_2(img)

        return img

    @staticmethod
    def apply_style_1(img):
        # Apply a specific style to the QR code (e.g., change colors)
        img = img.convert("RGB")
        pixels = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if pixels[i, j] == (0, 0, 0):
                    pixels[i, j] = (0, 128, 128)
        return img

    @staticmethod
    def apply_style_2(img):
        # Apply another style to the QR code (e.g., add a pattern)
        img = img.convert("RGB")
        pixels = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if pixels[i, j] == (0, 0, 0):
                    pixels[i, j] = (128, 0, 128)
        return img
