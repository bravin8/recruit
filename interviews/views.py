import json
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse

from accounts.models import BaseUser

def available(request, bu_id):
	user = BaseUser.objects.get(id=bu_id)

	if request.method == 'GET':
		context = {'user': user.first_name, 'timezone': ''}

	if request.method == 'POST':
		availability = json.loads(request.POST.get('availability'))
		for day, time in availability.items():
			print(day, time['start'], time['end'])
		context = {'message': 'success'}
		return JsonResponse({'message':'Availability Updated'})

	return render(request, 'interviews/available.html', context)