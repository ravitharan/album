from PIL import Image

def change_size(photo_name):
    size_300 = (300,300)
    photo = Image.open(photo_name)
    photo.thumbnail(size_300)
    photo.save("example.jpg")
