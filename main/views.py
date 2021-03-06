from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from .models import Ticket
from comments.models import Comment
from django.db.models import Count
from comments.forms import CommentForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView

class TicketListView(ListView): # generic list view, variable passed is object_list
    model = Ticket
    ordering = ['-date']
    paginate_by = 10
    
    def get_queryset(self):
        kwargs={}
        if 'qa' in self.request.GET:
            if self.request.GET['qa'] != 'all':
                kwargs['ticket_type'] = self.request.GET['qa']
            if self.request.GET['qb'] != 'all' :
                kwargs['status'] = self.request.GET['qb']
                # aggregate the number of comments
        return Ticket.objects.filter(**kwargs).annotate(num_comments=Count('comment')).order_by('-date')


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['title', 'ticket_type', 'status', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    fields = ['title', 'ticket_type', 'status', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.author:
            return True
        return False

class TicketDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    success_url = '/'

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.author:
            return True
        return False

def about(request):
    return render(request, 'main/about.html')

def votetoggle(request, pk):
    obj = get_object_or_404(Ticket, pk=pk)
    user = request.user
    if user.is_authenticated:
        if user in obj.votes.all():
            obj.votes.remove(user)
        else:
            obj.votes.add(user)
    return redirect('ticket-detail', pk)

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    user = request.user
    comments = Comment.objects.filter(ticket=ticket)
    if request.method == 'POST':
        if user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                    comment_form.instance.user = user
                    comment_form.instance.ticket = ticket
                    comment_form.save()
                    return redirect('ticket-detail', pk)
            else:
                comment_form = CommentForm()
        else:
            messages.error(request, 'Please login to comment')
            comment_form = CommentForm()
    else:
            comment_form = CommentForm()
    return render(request, 'main/ticket_detail.html', {"object": ticket, "pk":pk, "comments": comments, 'comment_form': comment_form})

def search_tickets(request):
    tickets = Ticket.objects.filter(title=request.GET['q']).annotate(num_comments=Count('comment')).order_by('-date')
    return render(request, "main/ticket_list.html", {"object_list": tickets})