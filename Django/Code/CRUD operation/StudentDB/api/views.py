from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


"""
for class based view

from django.utils.decorators import method_decorator
from django.views import View
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        rest of the code will be same
    def post(self, request, *args, **kwargs):
        rest of the code will be same
    def put(self, request, *args, **kwargs):
        rest of the code will be same
    def delete(self, request, *args, **kwargs):
        rest of the code will be same
"""


@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
        else:
            stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Saved Successfully.'}
        else:
            res = {'msg': 'Please provide valid data.'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        #serializer = StudentSerializer(stu, data=pythondata) if we want to use put which means we have to provide all data to update database
        serializer = StudentSerializer(stu, data=pythondata, partial=True) #patch for updating specific data
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Updated'}
        else:
            res = {'msg': 'Some problem occured'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream) 
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data Deleted.'}
        #json_data = JSONRenderer().render(res)
        #return HttpResponse(json_data, content_type='application/json')   
        return JsonResponse(res, safe=False)   