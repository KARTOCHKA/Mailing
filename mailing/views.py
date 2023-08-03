from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from mailing.forms import ClientForm, MailingForm
from mailing.models import *
from mailing.services import MessageService, delete_task, send_mailing


class MailingListView(LoginRequiredMixin, generic.ListView):
    """Представление для просмотра рассылок"""
    model = Mailing
    extra_context = {'title': 'Рассылки'}

    def get_queryset(self):
        """Функция, позволяющая просматривать только свои рассылки для пользователя, который не является менеджером"""
        user = self.request.user
        if user.is_superuser or user.is_staff:
            queryset = Mailing.objects.all()
        else:
            queryset = Mailing.objects.filter(user=user)

        queryset = queryset.filter(is_published=True)
        return queryset


class MailingCreateView(LoginRequiredMixin, generic.CreateView):
    """Представление для создание рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_queryset(self):
        user = self.request.user
        mailing = Mailing.objects.all()
        if user.is_staff or user.is_superuser:
            queryset = mailing
        else:
            queryset = mailing.client.filter(user=user)
        return queryset

    def form_valid(self, form):
        """Если форма валидна, то при создании рассылки запускается периодическая задача и изменяется статус рассылки"""
        mailing = form.save(commit=False)
        mailing.user = self.request.user
        mailing.status = 'CREATE'
        mailing.save()

        message_service = MessageService(mailing)
        send_mailing(mailing)
        message_service.create_task()
        mailing.status = 'START'
        mailing.save()

        return super(MailingCreateView, self).form_valid(form)


class MailingUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Представление для изменения рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Представление для удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


def toggle_status(request, pk):
    """Функция, позволяющая отключать и активировать рассылку"""
    mailing = get_object_or_404(Mailing, pk=pk)
    message_service = MessageService(mailing)
    if mailing.status == 'START' or mailing.status == 'CREATE':
        delete_task(mailing)
        mailing.status = 'FINISH'
    else:
        message_service.create_task()
        mailing.status = 'START'

    mailing.save()

    return redirect(reverse('mailing:mailing_list'))


class ClientListView(LoginRequiredMixin, generic.ListView):
    """Представление для просмотра клиентов"""
    model = Client
    extra_context = {'title': 'Клиенты'}

    def get_queryset(self):
        """Функция, позволяющая просматривать только своих клиентов для пользователя, который не является менеджером"""
        user = self.request.user
        if user.is_staff or user.is_superuser:
            queryset = Client.objects.all()
        else:
            queryset = Client.objects.filter(user=user)

        queryset = queryset.filter(is_active=True)
        return queryset


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    """Представление для просмотра конкретного клиента"""
    model = Client


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    """Представление для создания клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        client = form.save(commit=False)
        client.user = self.request.user
        client.save()
        return super(ClientCreateView, self).form_valid(form)


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Представление для изменения клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    """Представление для удаления клиента"""
    model = Client
    success_url = reverse_lazy('mailing:client_list')
    permission_required = 'mailing.delete_client'


class MailingLogListView(LoginRequiredMixin, generic.ListView):
    """Представление для просмотра всех попыток рассылок"""
    model = MailingLogs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Попытки рассылки"
        context['log_list'] = MailingLogs.objects.all()
        return context
