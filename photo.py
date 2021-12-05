from PIL import Image
import glob

#pull image and show information, using working directory
img = Image.open('C:/Users/USER/Desktop/Software Training/Project - photo album/myimg.jpg')
print ('format: {}'.format(img.format))
print ('size: {}'.format(img.size))
print ('image mode: {}'.format(img.mode))
img.show()

#convert - jpg/png
#img = Image.open('C:/Users/USER/Desktop/Software Training/Project - photo album/myimg.jpg').convert("RGB")
#img.save("output.png","png")

#resize images
for (i, filename) in enumerate(glob.glob('C:/Users/USER/Desktop/Software Training/Project - photo album/*.jpeg')):
    print(filename)
    img = Image.open(filename).resize((600,600))
    img.save('{}{}{}'.format('C:/Users/USER/Desktop/Software Training/Project - photo album/resized',i+1,'.jpeg'))
    
#rotate image
#rotate_img = img.rotate(45)
#rotate_img.show()

#overlay shape onto image
img_with_shape = img.copy()
ImageDraw.Draw(img_with_shape).rectangle([(650,70),(830,210)])
img_with_shape.show()


