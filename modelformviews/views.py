from modelformviews.models import Student
from django.shortcuts import render,HttpResponseRedirect

from .forms import sturesgistration
from .models import Student
from rest_framework import viewsets
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
import requests



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    


    def student_list(request):
        Students = Student.objects.all()
            
        if request.method == 'GET': 
            student_serializer = StudentSerializer(Students, many=True)
            return JsonResponse(student_serializer.data, safe=False)
        
    def student_detail(request, pk):
        try: 
            Students = Student.objects.get(pk=pk) 
        except Student.DoesNotExist: 
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
        if request.method == 'GET': 
            student_serializer = StudentSerializer(Students) 
            return JsonResponse(student_serializer.data) 
    
        elif request.method == 'PUT': 
            student_data = JSONParser().parse(request) 
            student_serializer = StudentSerializer(Students, data=student_data) 
            if student_serializer.is_valid(): 
                student_serializer.save() 
                return JsonResponse(student_serializer.data) 
            return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

def add_stu(request):
    if request.method == 'POST':
        fm = sturesgistration(request.POST)
        if fm.is_valid(): 
            fm.save()
    else:
        fm = sturesgistration()
        
    return render(request,'contact_form.html', {'form': fm})            
   



# Create your views here.

def delete_stu(request):
    if request.method == 'POST':
        p=Student.objects.get(pk=id)
        p.delete()
        HttpResponseRedirect('/')

def show(request):
        fm = sturesgistration()
        stu=Student.objects.all()
        return render(request,'contact_list.html', {'object_list':stu})   
        
               


