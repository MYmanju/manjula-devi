import qrcode

name="manjula devi"
age=int(17)
ed_class="B.Tech 1st year"
course="CSC"
phone_no=int(9603186618)

data={'name':name,'age':age,'class':ed_class,'course':course,'phone number':phone_no}


qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=2,
)

qr.add_data(data)
qr.make(fit=True)

img=qr.make_image(fill_color="white",back_color="black")
img.save('hello.png')
img.show()
