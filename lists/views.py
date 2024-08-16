from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item, List
from django.core.exceptions import ValidationError
from .forms import ItemForm, ExistingListItemForm

def home_page(request):
    return render(request, "lists/home.html", {'form': ItemForm()})

def view_list(request, pk):   
    list_ = List.objects.get(id=pk) 
    items = Item.objects.filter(list=list_)
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'lists/list.html', {'list': list_, 'form': form, 'items': items})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'lists/home.html', {'form': form})
