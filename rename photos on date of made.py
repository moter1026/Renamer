import os
import random
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

path = './'  # Замените на фактический путь к вашей папке

list_of_file = os.listdir(path)
new_list_of_file = []
for ind in list_of_file:
    if ".jpg" in ind:
        new_list_of_file.append(ind)

def получить_дату_съемки(путь):
    # Открываем изображение
    изображение = Image.open(путь)

    # Получаем метаданные (Exif)
    метаданные = изображение._getexif()

    if метаданные is not None:
        for тег, значение in метаданные.items():
            тег_имя = TAGS.get(тег, тег)
            if тег_имя == 'DateTimeOriginal':
                return datetime.strptime(значение, '%Y:%m:%d %H:%M:%S')

    return None

# Сортировка списка фотографий по дате съемки
отсортированные_фото = sorted(new_list_of_file, key=получить_дату_съемки)

# listNames = []
for фото in enumerate(отсортированные_фото):
    os.rename(фото[1], str(фото[0]) + ".jpg")
    # while 1:
    #     randNum = random.randint(1001,2000)
    #     if not(randNum in listNames):
    #         os.rename(фото[1], str(randNum) + ".jpg")
    #         listNames.append(randNum)
    #         break
    #         # os.rename(фото[1], str(фото[0]) + ".jpg")
