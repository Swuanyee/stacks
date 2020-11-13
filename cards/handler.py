import openpyxl
from django.db import models
from openpyxl_image_loader import SheetImageLoader
from .models import CardsQuestion
import os


def test(f):
    excel = f
    print('start handling')
    wb = openpyxl.load_workbook(excel)
    worksheet = wb["Sheet1"]
    image_loader = SheetImageLoader(worksheet)
    excel_data = list()
    image = None

    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            if cell.value is None:
                cell.value = ''
            row_data.append(str(cell.value))

        num = cell.coordinate
        if image_loader.image_in(num):
            image = image_loader.get(num)
            name = str(num)
            image_format = '.' + str(image.format).lower()
            if image.format == "PNG":
                image.save('media/image/random.png')
                os.rename('media/image/random.png',
                          'media/image/' + name + image_format)
            elif image.format == "JPEG":
                image.save('media/image/random.jpeg')
                os.rename('media/image/random.jpeg',
                          'media/image/' + name + image_format)
            elif image.format == "JPG":
                image.save('media/image/random.jpg')
                os.rename('media/image/random.jpg',
                          'media/image/' + name + image_format)
        else:
            image = None

        if image:
            image = 'image/' + name + image_format
            card = CardsQuestion.objects.create(
                questionText=row_data[0],
                answerText=row_data[1],
                answerImage=image
            )
        else:
            card = CardsQuestion.objects.create(
                questionText=row_data[0],
                answerText=row_data[1])
        excel_data.append(row_data)
    return excel_data
