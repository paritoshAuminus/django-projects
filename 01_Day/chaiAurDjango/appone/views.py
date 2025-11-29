from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety

# Create your views here.
def appone(request):
    allFoods = ChaiVariety.objects.all()
    return render(request, 'appone/index.html', {'allFoods': allFoods})

def foodDetails(request, food_id):
    details = get_object_or_404(ChaiVariety, pk=food_id)
    return render(request, 'appone/food_details.html', {'details': details})