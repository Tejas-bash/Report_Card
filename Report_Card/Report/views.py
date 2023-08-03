from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q,Sum
from .seed import *

def get_students(request):

    queryset = Student.objects.all()
    
    if request.GET.get('search'):
        Search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = Search) |
            Q(department__department__icontains = Search) |
            Q(student_id__student_id__icontains = Search) |
            Q(student_email__icontains = Search)
        )
    # Boolean Opeartion
    page_number = request.GET.get("page",1)
    paginator = Paginator(queryset, 15)   # Pagination
    try:
        page_obj = paginator.page(page_number)
    except EmptyPage:
        page_obj = paginator.page(1)

    return render(request,'students.html',{'queryset':page_obj})


def see_marks(request,student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    return render(request,'see_marks.html',{'queryset':queryset,'total':total_marks})

