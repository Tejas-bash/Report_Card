from faker import Faker

fake = Faker()

import random

from .models import *

from django.db.models import *

def create_subject_marks(n):
    try:
        student_obj = Student.objects.all()
        subjects = Subject.objects.all()
        for student in student_obj:
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0,100),
                )
    except Exception as e:
        print(e)


def generate_report_card():
    ranks = Student.objects.annotate(marks = Sum('subjectmarks__marks')).order_by('-marks','-student_age')

    for i, rank in enumerate(ranks, start=1):
        ReportCard.objects.create(
        student = rank,
        student_rank = i
        )


def seed_db(n=10) -> None:
    try:
        for _ in range(n):
            departments_objs = Department.objects.all()
            random_index = random.randint(0,len(departments_objs)-1)
            department = departments_objs[random_index]
            student_id = f'STU-0{random.randint(100,900)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
                    )
    except Exception as e:
        print(e)