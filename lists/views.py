from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item, List

def home_page(request):
    return render(request, "lists/home.html")

def view_list(request, pk):   
    list_ = List.objects.get(id=pk) 
    items = Item.objects.filter(list=list_)
    return render(request, 'lists/list.html', {'items': items, 'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.pk}/')
def add_item(request, pk):
    list_ = List.objects.get(id=pk)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f"/lists/{list_.id}/")