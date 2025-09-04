import qrcode
from PIL import Image, ImageDraw, ImageFont

# URL pública de tu formulario en GitHub Pages
url = "https://dianalvgarcia.github.io/Soporte-TI-UPAEP/"

# Crear QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

img_qr = qr.make_image(fill_color="purple", back_color="white").convert("RGB")

# Agregar título arriba del QR
draw = ImageDraw.Draw(img_qr)
try:
    font = ImageFont.truetype("arialbd.ttf", 40)  # Arial Bold
except:
    font = ImageFont.load_default()

titulo = "SOPORTE TI PUEBLA"
w, h = draw.textbbox((0,0), titulo, font=font)[2:]  # Ancho y alto del texto
img_width, img_height = img_qr.size

# Crear imagen final con espacio para el título
new_height = img_height + h + 20
img_final = Image.new("RGB", (img_width, new_height), "white")
img_final.paste(img_qr, (0, h + 20))

draw = ImageDraw.Draw(img_final)
draw.text(((img_width - w) // 2, 10), titulo, font=font, fill="purple")

# Guardar QR
img_final.save("QR_SOPORTE_TI_PUEBLA.png")
print("QR generado correctamente: QR_SOPORTE_TI_PUEBLA.png")
