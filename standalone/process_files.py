import json
import os
import shutil
import glob
from PIL import Image
from pathlib import Path

from metadata import *

DST_FOLDER          = ".images"
ORG_FOLDER          = "original"
THUMBNAIL_FOLDER    = "thumbnail"

DATABASE_FILE   = ".database.json"
THUMBNAIL_SIZE  = (640, 480)

FILE_NAME_KEY       = 'file_name'
FILE_SIZE_KEY       = 'file_size'
IMAGE_PATH_KEY      = 'image_path'
THUMBNAIL_PATH_KEY  = 'thumbnail_path'

def update_database(data, file_name):
    with open(file_name, 'w') as fp:
        json.dump(data, fp)

def retrive_database(file_name):
    with open(file_name) as fp:
        data = json.load(fp)
    return data

def add_picture(image):
    if not os.path.exists(image):
        print(f'Error!, {image} cannot be accessed')
        return

    image_name = os.path.basename(image)
    image_size = os.stat(image).st_size

    image_metadata = get_exif_tags(image)
    image_metadata[FILE_NAME_KEY] = image_name
    image_metadata[FILE_SIZE_KEY] = image_size

    root_path = Path('..') / DST_FOLDER
    image_path = root_path / ORG_FOLDER
    if not image_path.exists():
        image_path.mkdir(parents=True)
    image_path = image_path / image_name

    thumbnail_path = root_path / THUMBNAIL_FOLDER
    if not thumbnail_path.exists():
        thumbnail_path.mkdir(parents=True)
    thumbnail_path = thumbnail_path / image_name

    database_path = root_path / DATABASE_FILE
    if database_path.exists():
        data = retrive_database(str(database_path))
    else:
        data = []

    already_exist = False
    for item in data:
        if (item['file_name'] == image_metadata['file_name']
            and item['file_size'] == image_metadata['file_size']):
            print(f'image {image} already exist')
            already_exist = True
            break
    if not already_exist:
        shutil.copy(image, str(image_path))
        image = Image.open(image)
        image.thumbnail(THUMBNAIL_SIZE)
        image.save(thumbnail_path)

        image_metadata[IMAGE_PATH_KEY] = str(image_path)
        image_metadata[THUMBNAIL_PATH_KEY] = str(thumbnail_path)
        data.append(image_metadata)
        update_database(data, str(database_path))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Argument error\nUsage: {sys.argv[0]} <picture_folder>\n')
        exit(1)
    photos_glob = os.path.join(sys.argv[1], '*.jpg')
    for photo in glob.glob(photos_glob):
        print(os.path.basename(photo))
        add_picture(photo)
