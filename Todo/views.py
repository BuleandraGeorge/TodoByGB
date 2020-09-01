from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
# Create your views here.


def todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "Todo/todo_list.html", context)


def add_task(request):

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, "Todo/add_task.html", context)


def edit_task(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, "Todo/edit_task.html", context)


def toggle_task(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('list')


def delete_task(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('list')
