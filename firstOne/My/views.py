from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety, Store
from .forms import ChaiVarietyForm

def all_my(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'My/all_My.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'My/chai_details.html', {'chai': chai})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']  
            stores = Store.objects.filter(chai_varieties=chai_variety)  
    else:
        form = ChaiVarietyForm()

    return render(request, 'My/chai_stores.html', {'stores': stores, 'form': form})
