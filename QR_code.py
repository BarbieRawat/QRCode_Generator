import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=b5Zay_Hd_7Q")
img.save("qr_code.png")
