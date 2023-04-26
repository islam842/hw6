from django.shortcuts import get_object_or_404
from phone_app.models import Phones
from phone_app.forms import ShowForm
from django.views import generic
from . import models, forms


# Create your views here.

# Не полная информация
class PhoneListView(generic.ListView):
    template_name = 'phone_list.html'
    queryset = Phones.objects.all()

    def get_queryset(self):
        return Phones.objects.all()


# Подробная информация
class PhoneDetailView(generic.DetailView):
    template_name = 'phone_detail.html'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(Phones, id=phone_id)


# Добавить новый телефон
class CreatePhoneView(generic.CreateView):
    template_name = 'crud/create_phone.html'
    form_class = ShowForm
    queryset = Phones.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePhoneView, self).form_valid(form=form)


# Список телефонов для удаления
class DeletePhoneListView(generic.ListView):
    template_name = 'crud/phone_list_delete.html'
    queryset = Phones.objects.all()

    def get_queryset(self):
        return Phones.objects.all()


# удалить телефон  основная логика
class DeletePhoneView(generic.DeleteView):
    template_name = 'crud/phone_delete.html'
    success_url = '/phone_delete_list/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(Phones, id=phone_id)


# Список телефонов для изменения
class UpdatePhoneListView(generic.ListView):
    template_name = 'crud/phone_list_update.html'
    queryset = Phones.objects.all()

    def get_queryset(self):
        return Phones.objects.all()


# Изменить телефон
class UpdatePhoneView(generic.UpdateView):
    template_name = 'crud/phone_update.html'
    form_class = ShowForm
    success_url = '/phone_update_list/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(Phones, id=phone_id)

    def form_valid(self, form):
        return super(UpdatePhoneView, self).form_valid(form=form)


# Поиск телефонов
class SearchView(generic.ListView):
    template_name = 'phone_list.html'
    context_object_name = 'phone'
    paginate_by = 5

    def get_queryset(self):
        return Phones.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


# для отзыва
class CreateCommentView(generic.CreateView):
    """
    Добавление отзыва
    """
    template_name = 'phone_detail.html'
    form_class = forms.CommentForm
    queryset = models.Reviews.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateCommentView, self).form_valid(form=form)