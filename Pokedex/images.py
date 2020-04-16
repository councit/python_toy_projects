from PIL import Image, ImageFilter

img = Image.open('./assests/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)

filtered_img.show()
