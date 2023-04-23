from django.shortcuts import render, get_object_or_404
from phone_app.models import Phones
from phone_app.forms import ShowForm
from django.http import HttpResponse


# Create your views here.

# не полная информация
def phone_all_view(request):
    phone_list = Phones.objects.all()
    context = {
        'phone_list': phone_list
    }
    return render(request, 'phone_list.html', context)


# детальная информация
def phone_detail_view(request, id):
    phone_id = get_object_or_404(Phones, id=id)
    context = {
        'phone_id': phone_id
    }
    return render(request, 'phone_detail.html', context)


# Добавить новый телефон
def create_phone_view(request):
    method = request.method
    if method == "POST":
        form = ShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Телефон успешно добавлен')
    else:
        form = ShowForm()
    return render(request, 'crud/create_phone.html', {'form': form})


# Список телефонов для удаления
def delete_phone_list_view(request):
    phone_list_delete = Phones.objects.all()
    return render(request, 'crud/phone_list_delete.html', {'phone_list_delete': phone_list_delete})


# Список для удаления по id номером
def phone_delete_detail_view(request, id):
    phone_delete_id = get_object_or_404(Phones, id=id)
    return render(request, 'crud/phone_id_delete.html',
                  {'phone_id_delete': phone_delete_id})


# удалить телефон  основная логика
def delete_phone_view(request, id):
    phone_id = get_object_or_404(Phones, id=id)
    phone_id.delete()
    return HttpResponse('Телефон успешно удален')



# Список телефонов для изменения
def update_phone_list_view(request):
    phone_list_update = Phones.objects.all()
    return render(request, 'crud/phone_list_update.html', {'phone_list_update': phone_list_update})


#Изменить телефон
def update_phone_view(request, id):
    phone_id = get_object_or_404(Phones, id=id)
    if request.method == 'POST':
        form = ShowForm(instance=phone_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Телефон успешно изменен')
    else:
        form = ShowForm(instance=phone_id)

    context = {
        'form': form,
        'phone_id': phone_id
    }

    return render(request, 'crud/phone_update.html', context)