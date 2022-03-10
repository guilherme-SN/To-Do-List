from django.shortcuts import render, HttpResponseRedirect
from .models import Item, ToDoList
from .forms import CreateNewToDo

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():
        if response.method == 'POST':
            if response.POST.get('save'):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == 'clicked':
                        item.checkComplete = True
                    else:
                        item.checkComplete = False
                    item.save()
            elif response.POST.get('new'):
                txt = response.POST.get('newItem')
                if len(txt) > 2:
                    ls.item_set.create(txt=txt, checkComplete=False)    
                else:
                    print('Invalid')
            else:
                for item in ls.item_set.all():
                    if response.POST.get('d' + str(item.id)) == 'delete':
                        item.delete()
                        ls.save()
                    elif response.POST.get('u' + str(item.id)) == 'update':
                        print('etnre')
                        return HttpResponseRedirect(f'/update/{id}/{item.id}')
                        
        return render(response, 'main/list.html', {"ls": ls})
    return render(response, 'main/view.html', {})


def home(response):
    return render(response, 'main/home.html', {})


def create(response):
    if response.method == 'POST':
        form = CreateNewToDo(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect('/%i' %t.id)
    else:
        form = CreateNewToDo()
    return render(response, 'main/create.html', {"form": form})


def view(response):
    return render(response, 'main/view.html', {})


def update(response, id_td, id_item):
    ls = ToDoList.objects.get(id=id_td)
    item = ls.item_set.get(id=id_item)

    if response.method == 'POST':
        print(response.POST)
        item.txt = response.POST.get('ntext')
        item.save()
        return HttpResponseRedirect(f'/{id}')
        
    return render(response, 'main/update.html', {"text": item})