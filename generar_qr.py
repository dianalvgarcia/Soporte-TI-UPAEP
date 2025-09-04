import qrcode

# URL de tu formulario en GitHub Pages
url = "https://dianalvgarcia.github.io/Soporte-TI-UPAEP/"

# Generar el código QR
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(url)
qr.make(fit=True)

# Crear una imagen del QR
img = qr.make_image(fill='black', back_color='white')

# Guardar la imagen
img.save("qr_formulario.png")

print("QR generado con éxito: qr_formulario.png")
