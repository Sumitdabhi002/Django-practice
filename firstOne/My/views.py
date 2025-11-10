from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

def all_my(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'My/all_My.html', {'chais': chais})

def chai_detail(request,chai_id):
    chai = get_object_or_404(ChaiVariety,pk=chai_id)
    return render(request,'my/chai_details.html',{'chai':chai})
