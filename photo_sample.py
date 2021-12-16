from PIL import Image
import os

THUMPNAIL_SIZE = 240

def create_thumbnail(folder, max_thumbnail_size):
    image_list = []
    for pic in os.listdir(folder):
        if pic.endswith('.jpg'):
            image = Image.open(pic)
            w = image.width
            h = image.height
            shrink_ratio_width = w / max_thumbnail_size
            shrink_ratio_height = h / max_thumbnail_size
            if shrink_ratio_height > shrink_ratio_width:
                shrink_ratio = shrink_ratio_height
            else:
                shrink_ratio = shrink_ratio_width
            thumbnail_size = (w / shrink_ratio,h / shrink_ratio)
            fn, fext = os.path.splitext(pic)
            image.thumbnail(thumbnail_size)
            image.save('thumbnail/_thumb{}{}'.format(fn, fext))
            image_list.append(pic)
    return image_list


#output to html file
def htmlfile(images_names):
    html_file = open('website.html', 'w')

    top_html = "<!DOCTYPE html>\n<html>\n<body>\n\n<!-- images -->\n<table>\n\n"
    bottom_html = "\n</table>\n</body>\n</html>"

    html_file.write(top_html)

    pic_count = 0
    for bigimage in images_names:

        if pic_count % 3 == 0: # Start next row
            html_file.write("<tr height=\"%d\">\n" % (THUMPNAIL_SIZE))

        #Write a column
        html_file.write("<td width=\"%d\"> " % (THUMPNAIL_SIZE))
        html_file.write("<a href=\"%s\"><img src=\"thumbnail/_thumb%s\"></a> " % (bigimage, bigimage))
        html_file.write("</td>\n")

        if pic_count % 3 == 2: # End row
            html_file.write("</tr>\n\n")
        pic_count += 1

    if pic_count % 3 != 0: # If end row is not written before, write it now
        html_file.write("</tr>\n\n")

    html_file.write(bottom_html)


if __name__ == "__main__": 
    images_names = create_thumbnail('.', THUMPNAIL_SIZE)
    htmlfile(images_names)
    print("Following pictures copied:")
    for bigimage in images_names:
        print(bigimage)

