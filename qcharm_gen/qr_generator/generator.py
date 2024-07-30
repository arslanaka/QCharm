import qrcode
from PIL import Image


class QRCodeGenerator:
    @staticmethod
    def generate(data, file_path, fill_color="black", back_color="white"):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(file_path)
