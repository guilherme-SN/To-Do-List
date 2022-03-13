from django import forms


class CreateNewToDo(forms.Form): # this form is used to create a new task
    name = forms.CharField(label='Name', max_length=300)
    check = forms.BooleanField(required=False)