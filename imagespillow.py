from PIL import Image
import os
import webbrowser

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
            print(w / h, w, h)
            thumbnail_size = (w / shrink_ratio,h / shrink_ratio)
            fn, fext = os.path.splitext(pic)
            image.thumbnail(thumbnail_size) 
            image.save('thumbnail/_thumb{}{}'.format(fn, fext))
            print('image thumbnail saved as', image)
            image_list.append(pic)
    return image_list

images_names = create_thumbnail('.', 240)

print(images_names)

#output to html file

def htmlfile(images_names): 
    is_it_3 = 0
    html_file = open('website.html', 'w')
    top_html = '''<!DOCTYPE html>
<html>
<body>

<!-- images -->
<table>
<tr>'''
    table_break = '''</tr>
<tr>'''
    html_file.write(top_html)
    for bigimage in images_names:
        new_html = '''<td><a href="%s"><img src="thumbnail/_thumb%s"></a></td>''' 
        new_realhtml = new_html % (bigimage, bigimage)
        html_file.write(new_realhtml)
        is_it_3 += 1
        if is_it_3 % 3 == 0:
            html_file.write(table_break)
    bottom_html = '''</tr>
    
</table>

</body>
</html>'''
    html_file.write(bottom_html)

htmlfile(images_names)
