import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
from qcharm_gen.qr_generator.generator import QRCodeGenerator
from qcharm_gen.qr_generator.utils import choose_color


class QRCodeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QR Code Generator with Customization")
        self._setup_ui()

    def _setup_ui(self):
        self.label = tk.Label(self.root, text="Enter data:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=5)

        self.color_label = tk.Label(self.root, text="Choose QR Code Colors")
        self.color_label.pack(pady=10)

        self.generate_button = tk.Button(self.root, text="Generate QR Code", command=self.generate_and_display_qr)
        self.generate_button.pack(pady=10)

        self.panel = tk.Label(self.root)
        self.panel.pack(pady=10)

    def generate_and_display_qr(self):
        data = self.entry.get()
        if not data:
            messagebox.showwarning("Input Error", "Please enter some data")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not file_path:
            return

        fill_color = choose_color(self.root, "Choose fill color")
        back_color = choose_color(self.root, "Choose background color")

        QRCodeGenerator.generate(data, file_path, fill_color, back_color)
        img = Image.open(file_path)
        img = img.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.panel.config(image=img)
        self.panel.image = img
        messagebox.showinfo("Success", "QR Code generated and saved successfully!")

    def run(self):
        self.root.mainloop()
