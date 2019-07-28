from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Message

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['subject', 'message']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)