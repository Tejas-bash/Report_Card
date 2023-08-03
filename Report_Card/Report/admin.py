from django.contrib import admin
from .models import *
from django.db.models import *


admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)

admin.site.register(Subject)
@admin.register(SubjectMarks)
class SubjectMarksadmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']


@admin.register(ReportCard)
class ReportCardadmin(admin.ModelAdmin):
    list_display = ['student','student_rank','total_marks','Date_of_report_card_generation']
    ordering = ['student_rank']

    def total_marks(self,obj):
        subject_marks = SubjectMarks.objects.filter(student = obj.student)
        print(subject_marks)
        return subject_marks.aggregate(marks = Sum('marks'))['marks']