from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from applications.globals.models import (Designation, ExtraInfo,
                                         HoldsDesignation, DepartmentInfo)
from applications.academic_information.models import *
import xlrd

# Create your views here.

@login_required
def view_alloted_room(request):
    hall_1_student = Student.objects.filter(hall_no=1)
    hall_3_student = Student.objects.filter(hall_no=3)
    hall_4_student = Student.objects.filter(hall_no=4)[:10]                        

    context = {
        'hall_1_student': hall_1_student,
        'hall_3_student': hall_3_student,
        'hall_4_student': hall_4_student
    }

    return render(request, 'hostelmanagement/hostel.html', context)


def add_hall_room(request):
    if request.method == "POST":
        files = request.FILES['hall4room']
        excel = xlrd.open_workbook(file_contents=files.read())
        if str(excel.sheets()[0].cell(2,9).value) == 'Hall-4':
            hall_4_allotment = []
            for sheet in excel.sheets():
                for row in range(1, sheet.nrows):
                    roll_no = int(sheet.cell(row,1).value)
                    name = str(sheet.cell(row,2).value)
                    program = str(sheet.cell(row,4).value)
                    room_no = str(sheet.cell(row,7).value)
                    block = str(sheet.cell(row,8).value)
                    hall_4_allotment.append([roll_no, name, program, room_no, block])
            hall_4_allotment = hall_4_allotment[:10]

            
            context = {
                'hall_4_allotment': hall_4_allotment
            }
            return render(request, 'hostelmanagement/hostel.html', context)

        if str(excel.sheets()[0].cell(2,9).value) == 'Hall-3':
            hall_3_allotment = []
            for sheet in excel.sheets():
                for row in range(1, sheet.nrows):
                    roll_no = int(sheet.cell(row,1).value)
                    name = str(sheet.cell(row,2).value)
                    program = str(sheet.cell(row,4).value)
                    room_no = str(sheet.cell(row,7).value)
                    block = str(sheet.cell(row,8).value)
                    hall_3_allotment.append([roll_no, name, program, room_no, block])
            hall_3_allotment = hall_3_allotment[:10]

            
            context = {
                'hall_3_allotment': hall_3_allotment
            }
            return render(request, 'hostelmanagement/hostel.html', context)

        if str(excel.sheets()[0].cell(2,9).value)[:6] == 'Hall-1':
            print("insdie hall1")
            hall_1_allotment = []
            for sheet in excel.sheets():
                for row in range(1, sheet.nrows):
                    roll_no = int(sheet.cell(row,1).value)
                    name = str(sheet.cell(row,2).value)
                    program = str(sheet.cell(row,4).value)
                    room_no = str(sheet.cell(row,7).value)
                    block = str(sheet.cell(row,8).value)
                    hall_1_allotment.append([roll_no, name, program, room_no, block])
            hall_1_allotment = hall_1_allotment[:10]

            context = {
                'hall_1_allotment': hall_1_allotment
            }
            return render(request, 'hostelmanagement/hostel.html', context)

        return render(request, 'hostelmanagement/hostel.html')