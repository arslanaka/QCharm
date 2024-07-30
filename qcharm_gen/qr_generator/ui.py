import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
from qcharm_gen.qr_generator.generator import QRCodeGenerator


class QRCodeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QR Code Generator")
        self.root.geometry("400x500")
        self._setup_ui()

    def _setup_ui(self):
        # Input field for data
        self.label = tk.Label(self.root, text="Enter data:", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, width=40, font=("Helvetica", 12))
        self.entry.pack(pady=5)

        # Dropdown menu for QR styles
        self.style_label = tk.Label(self.root, text="Choose QR style:", font=("Helvetica", 14))
        self.style_label.pack(pady=10)

        self.qr_styles = ["Basic", "Style 1", "Style 2"]
        self.style_var = tk.StringVar(value=self.qr_styles[0])
        self.style_menu = ttk.Combobox(self.root, textvariable=self.style_var, values=self.qr_styles, state="readonly", font=("Helvetica", 12))
        self.style_menu.pack(pady=5)

        # Generate QR code button
        self.generate_button = tk.Button(self.root, text="Generate QR Code", command=self.generate_and_display_qr, font=("Helvetica", 14))
        self.generate_button.pack(pady=20)

        # Panel to display QR code
        self.panel = tk.Label(self.root)
        self.panel.pack(pady=10)

        # Save QR code button
        self.save_button = tk.Button(self.root, text="Save QR Code", command=self.save_qr_code, font=("Helvetica", 14))
        self.save_button.pack(pady=10)

    def generate_and_display_qr(self):
        data = self.entry.get()
        style = self.style_var.get()
        if not data:
            messagebox.showwarning("Input Error", "Please enter some data")
            return

        # Generate QR code
        qr_image = QRCodeGenerator.generate(data, style)

        # Update the panel with the QR code
        self.qr_image_tk = ImageTk.PhotoImage(qr_image)
        self.panel.config(image=self.qr_image_tk)
        self.panel.image = self.qr_image_tk

    def save_qr_code(self):
        if not hasattr(self, 'qr_image_tk'):
            messagebox.showwarning("Save Error", "Generate a QR code first")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not file_path:
            return

        self.qr_image_tk._PhotoImage__photo.write(file_path)

    def run(self):
        self.root.mainloop()
