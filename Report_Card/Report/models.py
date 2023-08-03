from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    class Meta:
        # Ordering the Department data on alphabetical order
        ordering = ['department']


class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id


class Subject(models.Model):
    subject_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.subject_name


class Student(models.Model):
    department = models.ForeignKey(
        Department, related_name='depart', on_delete=models.CASCADE)
    student_id = models.OneToOneField(
        StudentID, related_name='studentid', on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    # If Email id already there I will not other email id
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name

    class Meta:
        ordering = ['student_name']
        verbose_name = 'student'


class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name='subjectmarks',on_delete=models.CASCADE)  # Related_name targeted marks of each student
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.student.student_name} {self.subject.subject_name} {self.marks}'

    class Meta:
        unique_together = ['student', 'subject', 'marks']


class ReportCard(models.Model):
    student = models.ForeignKey(
        Student, related_name='studentreportmarks', on_delete=models.CASCADE)
    student_rank = models.IntegerField()
    Date_of_report_card_generation = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student_rank', 'Date_of_report_card_generation']
