from django.shortcuts import render
from django.http import JsonResponse
from aplikasi1.models import Course
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def apiCourse(request):
    if (request.method == "GET"):
        # Serialize the data into json        
        data = serializers.serialize("json", Course.objects.all())
        # Turn the JSON data into a dict and send as JSON response             
        return JsonResponse(json.loads(data), safe=False)

    if (request.method == "POST"):
        # Turn the body into a dict        
        body = json.loads(request.body.decode("utf-8"))
        # filter data        
        if not body:
                data = '{"message": "data is not json type!"}'            
                dumps = json.loads(data)
                return JsonResponse(dumps, safe=False)
        else:
            created = Course.objects.create(
                course_name=body['course_name']
            )
            data = '{"message": "data successfully created!"}'            
            dumps = json.loads(data)
            return JsonResponse(dumps, safe=False)
        
@csrf_exempt
def update_item(request, item_id):
    if request.method == 'PUT':
        item = next((item for item in data if item['id'] == item_id), None)
        if item is None:
            return JsonResponse({'error': 'Item not found'}, status=404)
        body = json.loads(request.body)
        item.update(body)
        return JsonResponse(item)

@csrf_exempt
def delete_item(request, item_id):
    if request.method == 'DELETE':
        global data
        data = [item for item in data if item['id'] != item_id]
        return JsonResponse({'message': 'Item deleted'}, status=200)