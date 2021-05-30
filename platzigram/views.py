from django.http import HttpResponse
import json


def hi(request):
    numbers = [int(number) for number in request.GET['numbers'].split(',')]
    data = {
        'status': 'Ok',
        'numbers': numbers,
        'message': 'Integers sorted successful'
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


def say_hi(request, name, edad):
    if edad < 18:
        message = f'Hola {name}, no tienes accceso'
    else:
        message = f'Hola {name}, bienvenido!'
    return HttpResponse(message)
