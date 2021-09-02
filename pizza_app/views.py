from django.http import HttpResponse,JsonResponse
from .serializers import PizzaSerializer
from .models import Piz_Mod
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def pizza_List(request):
    if request.method == 'GET':
        all_pizza= Piz_Mod.objects.all()
        serializer = PizzaSerializer(all_pizza, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if (data['type']== 'Regular' or data['type']== 'Square'):
            pizza_size=data['size']
            check_database=Piz_Mod.objects.filter(size=pizza_size)
            if(check_database):
                serializer = PizzaSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.errors, status=400)
            else:
                return HttpResponse(status=422)
        else:
            return HttpResponse(status=422)


@csrf_exempt
def pizza_Detail(request, pk):
    try:
        temp_pizza = Piz_Mod.objects.get(id=pk)
    except Piz_Mod.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PizzaSerializer(temp_pizza)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PizzaSerializer(temp_pizza, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        temp_pizza.delete()
        return HttpResponse(status=204)

@csrf_exempt
def pizza_size_and_type(request,ty,si):
    try:
        if (ty=='Square' or ty=='Regular'):
            temp_pizza = Piz_Mod.objects.filter(type=ty).filter(size=si)
    except Piz_Mod.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer=PizzaSerializer(temp_pizza,many=True)
        return JsonResponse(serializer.data,safe=False)
