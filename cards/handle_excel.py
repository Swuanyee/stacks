"""
This doc contains handler for any excel file uploaded by user.
"""


import openpyxl
from openpyxl_image_loader import SheetImageLoader
from .models import Deck, CardsQuestion
import os


def handle_excel(excel, deck):
    print('start handling excel')  # test
    """
    Get openpyxl to open a Sheet 1
    of the workbook
    """
    wb = openpyxl.load_workbook(excel)
    worksheet = wb["Sheet1"]
    # openpyxl_image_loader is needed
    # to handle images in excel file.
    image_loader = SheetImageLoader(worksheet)

    for row in worksheet.iter_rows():
        questionImage = None
        answerImage = None
        image = None
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
            cell_coordinate = cell.coordinate
            list_coordinate = list(cell_coordinate)
            if list_coordinate[0] == 'B':
                num = cell.coordinate
                if image_loader.image_in(num):
                    questionImage = image_loader.get(num)
                    qnsname = str(num) + str(deck.title).replace(" ", "") +\
                        str(deck.subject).replace(" ", "") +\
                        str(deck.creator).replace(" ", "")
                    print(qnsname)
                    image_format = '.' + str(questionImage.format).lower()
                    if questionImage.format == "PNG":
                        questionImage.save('media/images/cellimage.png')
                        os.rename('media/images/cellimage.png',
                                  'media/images/' + qnsname + image_format)
                    elif questionImage.format == "JPEG":
                        questionImage.save('media/images/cellimage.jpeg')
                        os.rename('media/images/cellimage.jpeg',
                                  'media/images/' + qnsname + image_format)
                    elif questionImage.format == "JPG":
                        questionImage.save('media/images/cellimage.jpg')
                        os.rename('media/images/cellimage.jpg',
                                  'media/images/' + qnsname + image_format)
            elif list_coordinate[0] == 'D':
                num = cell.coordinate
                if image_loader.image_in(num):
                    answerImage = image_loader.get(num)
                    ansname = str(num) + str(deck.title).replace(" ", "") +\
                        str(deck.subject).replace(" ", "") +\
                        str(deck.creator).replace(" ", "")
                    image_format = '.' + str(answerImage.format).lower()
                    if answerImage.format == "PNG":
                        answerImage.save('media/images/cellimage.png')
                        os.rename('media/images/cellimage.png',
                                  'media/images/' + ansname + image_format)
                    elif answerImage.format == "JPEG":
                        answerImage.save('media/images/cellimage.jpeg')
                        os.rename('media/images/cellimage.jpeg',
                                  'media/images/' + ansname + image_format)
                    elif answerImage.format == "JPG":
                        answerImage.save('media/images/cellimage.jpg')
                        os.rename('media/images/cellimage.jpg',
                                  'media/images/' + ansname + image_format)

        if questionImage:
            print(f'question image {questionImage}')
        elif answerImage:
            print(f'answer image {answerImage}')
        if row_data[0] != 'None' and\
                row_data[0] != 'Question' and\
                row_data[0] != 'Questions' and\
                row_data[0] != 'questions' and\
                row_data[0] != 'question':
            if questionImage is not None and answerImage is not None:
                answerImage = 'images/' + ansname + image_format
                questionImage = 'images/' + qnsname + image_format
                CardsQuestion.objects.create(
                    questionText=row_data[0],
                    questionImage=questionImage,
                    answerText=row_data[2],
                    answerImage=answerImage,
                    deck=deck)
            elif questionImage is None and answerImage is not None:
                answerImage = 'images/' + ansname + image_format
                CardsQuestion.objects.create(
                    questionText=row_data[0],
                    answerText=row_data[2],
                    answerImage=answerImage,
                    deck=deck)
            elif questionImage is not None and answerImage is None:
                questionImage = 'images/' + qnsname + image_format
                CardsQuestion.objects.create(
                    questionText=row_data[0],
                    questionImage=questionImage,
                    answerText=row_data[2],
                    deck=deck)
            else:
                CardsQuestion.objects.create(
                    questionText=row_data[0],
                    answerText=row_data[2],
                    deck=deck)
    print('end')
