from django.urls import path
import os
import json
from datetime import datetime
from . import views
from django.conf import settings

DST_FOLDER          = ".images"
ORG_FOLDER          = "original"
THUMBNAIL_FOLDER    = "thumbnail"
DATABASE_FILE       = ".database.json"

THUMBNAIL_NAME_KEY  = 'thumbnail'
FILE_NAME_KEY       = 'file_name'
FILE_SIZE_KEY       = 'file_size'
WIDTH_KEY           = 'width'
HEIGHT_KEY          = 'height'
DATE_KEY            = 'date'
TS_KEY              = 'ts'
LOCATION_KEY        = 'location'

urlpatterns = [
    path('', views.index, name='album'),
]


def retrive_database(file_name):
    with open(file_name) as fp:
        data = json.load(fp)
    return data

database_path = os.path.join(settings.STATICFILES_DIRS[0][1], DST_FOLDER, DATABASE_FILE)
print(database_path)
data = []
epoch = datetime.utcfromtimestamp(0)
if os.path.exists(database_path):
    items = retrive_database(database_path)
    for item in items:
        item[THUMBNAIL_NAME_KEY] = os.path.join(DST_FOLDER, THUMBNAIL_FOLDER, item[FILE_NAME_KEY])

        date = datetime.strptime(item[DATE_KEY], "%Y %m %d %H %M %S")
        item[DATE_KEY] = date.strftime("%d %b %Y %H:%M")
        item[TS_KEY] = (date - epoch).total_seconds()

        data.append(item)

    data.sort(key=lambda x: x[TS_KEY])
    print(f'images count {len(data)}')


