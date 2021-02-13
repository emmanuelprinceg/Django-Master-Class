from django.shortcuts import render
from django.http import HttpResponse
from .models import item
from django.template import loader
# Create your views here.
def index(request):
    item_list= item.objects.all()
    template=loader.get_template('food/index.html')
    context={
        'item_list':item_list,

    }
    return render(request,'food/index.html',context)

def items(request):
    return HttpResponse('This is an item view')

def detail(request,item_id):
    item1=item.objects.get(pk=item_id)
    context={
        'item1':item1,}
    return render(request,'food/detail.html',context)