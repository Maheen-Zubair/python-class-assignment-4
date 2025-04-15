import qrcode 

data = "hello world" #yeh woh data he qr mai store hoga
qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data) #data add ho arha he

qr.make(fit=True)  #fit=true ka mtb size will automatically adjust size
qr_img = qr.make_image(fill_color="blue", back_color="white")

qr_img.save("C:/Users/Hp/3D Objects/python/python-class-assignment-4/Ass- 01/03_Advanced/p3_qr_code_encoder_decoder/qr_code.png")