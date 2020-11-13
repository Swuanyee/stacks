"""bulk add users"""

import openpyxl
from users.models import CustomUser
import os
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password


def handle_excel(excel):
    print('start handling excel')
    wb = openpyxl.load_workbook(excel)
    worksheet = wb["Sheet1"]
    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        print(row_data)
        if row_data[0] != "first_name":
            try:
                update_user = CustomUser.objects.get(email=row_data[2])
                password = make_password(row_data[3])
                update_user.first_name = row_data[0]
                update_user.last_name = row_data[1]
                update_user.profile = row_data[4]
                update_user.save()
            except ObjectDoesNotExist:
                password = make_password(row_data[3])
                CustomUser.objects.create(first_name=row_data[0],
                        last_name=row_data[1],
                        email=row_data[2],
                        password=password,
                        profile=row_data[4])
