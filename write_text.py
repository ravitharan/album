from PIL import Image, ImageFont, ImageDraw
from PIL.ExifTags import TAGS
import sys

def write_text(img):
    img = Image.open(img)
    font = ImageFont.truetype("arial.ttf", 50)
    draw = ImageDraw.Draw(img)
    exifdata = img.getexif()
    text = ""
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id) 
        if isinstance(data, bytes):
            data = data.decode()
        if tag == "DateTime":
            text = data
    draw.text((400,400), text, (0, 0, 0), font = font)
    img.save("text.png")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <jpeg_file>\n')
        exit(1)
    image = sys.argv[1]

    write_text(image)
    
