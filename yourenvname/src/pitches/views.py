from django.shortcuts import render
from .models import pitches
# Create your views here.

def pitches_detail_views(request):
	obj = pitches.objects.get(id=1)
	context = {
	'object': obj
	}
	return render(request, "pitches/catch.html", context)