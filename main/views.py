from django.shortcuts import render, HttpResponseRedirect
from .models import Item, ToDoList
from .forms import CreateNewToDo


# Create your views here.
def index(response, id): # "main" view
    ls = ToDoList.objects.get(id=id)

    # check if the todo list belongs to the user that request it
    if ls in response.user.todolist.all():
        # check if we received a request
        if response.method == 'POST': 
            for item in ls.item_set.all():
                # this is responsible for check and save the status' whenever we clicked a taks to complete it
                if response.POST.get("c" + str(item.id)) == 'clicked' and item.checkComplete:
                    item.checkComplete = False
                elif response.POST.get("c" + str(item.id)) == 'clicked' and not item.checkComplete:
                    item.checkComplete = True
                item.save()
           
           # check if we want to create a new task
            if response.POST.get('new'):
                txt = response.POST.get('newItem')
                if len(txt) > 2:
                    ls.item_set.create(txt=txt, checkComplete=False)    
                else:
                    print('Invalid')
            else:
                for item in ls.item_set.all():
                    # check if we want to delete a task
                    if response.POST.get('d' + str(item.id)) == 'delete':
                        item.delete()
                        ls.save()
                    # check if we want to update a task
                    elif response.POST.get('u' + str(item.id)) == 'update':
                        print('etnre')
                        return HttpResponseRedirect(f'/update/{id}/{item.id}')            
        return render(response, 'main/list.html', {"ls": ls})
    return render(response, 'main/view.html', {})


def home(response):
    return render(response, 'main/home.html', {})


def create(response):
    # if we receive a request with data, we want to create a form with that data and save it
    if response.method == 'POST':
        form = CreateNewToDo(response.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            tdlist = ToDoList(name=name)
            tdlist.save()
            response.user.todolist.add(tdlist)

        return HttpResponseRedirect('/%i' %tdlist.id)
    else:
        form = CreateNewToDo()
    return render(response, 'main/create.html', {"form": form})


def view(response):
    return render(response, 'main/view.html', {})


def update(response, id_td, id_item):
    ls = ToDoList.objects.get(id=id_td)
    item = ls.item_set.get(id=id_item)

    if response.method == 'POST':
        item.txt = response.POST.get('newtext')
        item.save()
        return HttpResponseRedirect(f'/{id_td}')
    return render(response, 'main/update.html', {"text": item})