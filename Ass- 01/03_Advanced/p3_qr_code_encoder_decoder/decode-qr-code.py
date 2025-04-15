from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:/Users/Hp/3D Objects/python/python-class-assignment-4/Ass- 01/03_Advanced/p3_qr_code_encoder_decoder/qr_code.png")
result = decode(img)

print(result)