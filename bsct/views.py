"""
These views do nothing other than provide members of the 'plain' BSCT template
set as default template names.
"""
from django.views import generic

class AbstractBaseView():
    fields = '__all__'

class CreateView( AbstractBaseView, generic.CreateView ):
    template_name = 'bsct/plain/form.html'

class UpdateView( AbstractBaseView, generic.UpdateView ):
    template_name = 'bsct/plain/form.html'

class ListView( AbstractBaseView, generic.ListView ):
    template_name = 'bsct/plain/list.html'

class DetailView( AbstractBaseView, generic.DetailView ):
    template_name = 'bsct/plain/detail.html'

class DeleteView( AbstractBaseView, generic.DeleteView ):
    template_name = 'bsct/plain/confirm_delete.html'
