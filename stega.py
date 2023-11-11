from stegano import lsb
secret = lsb.hide("img.jpg", "hello dek")
secret.save("./rahasia.png")