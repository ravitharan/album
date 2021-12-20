import sys
from PIL import Image
import os

def covert_small_size(image,hight,width):
    """
        Big size photos change to small size photos
        
    """
    image_name = (os.path.split(image)[-1])
    image = Image.open(image_name)
    MAX_SIZE = (int(hight),int(width))
    image.thumbnail(MAX_SIZE)
    resize_image = image.save("COPY --"+image_name)

    return resize_image

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f'Argument error\nUsage: {sys.argv[0]} {sys.argv[1]} {sys.argv[2]} <jpeg_file>\n')
        exit(1)
    image = sys.argv[1]
    hight = sys.argv[2]
    width = sys.argv[3]
    resize_image = covert_small_size(image,hight,width)
