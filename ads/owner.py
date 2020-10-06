from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from ads.models import Articles

class OwnerListView(ListView):
    model = Articles
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles_list'] = Articles.objects.all()
        context['user'] = self.request.user
        context['ctx'] = context
        return context

class OwnerDetailView(DetailView):
    '''Same'''

class OwnerCreateView(LoginRequiredMixin, CreateView):
    '''Same'''

    def form_valid(self,form):
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    def get_queryset(self):
        query = super(OwnerUpdateView, self).get_queryset()
        return query.filter(owner=self.request.user)

class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    '''Same'''