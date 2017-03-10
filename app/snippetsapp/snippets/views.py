from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Snippets
from .forms import AddSnippet
from django.views.generic.edit import UpdateView

#  function to delete item from model and re render view
def delete_item(request, pk):
    # get item
    post = Snippets.objects.get(pk = pk)
    # delete it
    post.delete()
    snippets = Snippets.objects.all()
    form = AddSnippet()
    return render(request, 'index.html', {'form': form, "snippets": snippets, "error": ""})

#  function to select item for editing  render to view
def edit_item(request, pk):
    # get item
    primaryKey = pk
    item = Snippets.objects.get(pk = pk)
    snippets = Snippets.objects.all()
    form = AddSnippet()
    # edititem = EditSnippet(instance=item)
    return render(request, 'index.html', {'form': form, "snippets": snippets, 'edititem': item, "error": ""})

# function to edit based on pk
def update_item(request):
    error=""
    if request.method == 'POST':
        pk=request.POST.get("pk")
        newDict = {"title" : request.POST.get("title"),
        "language": request.POST.get("language"),
        "snippet" : request.POST.get("snippet"),
        "description" : request.POST.get("description") }
        # update and throw error message it duplicate title
        try:
            Snippets.objects.select_for_update().filter(pk=pk).update(**newDict)
        except:
            error = 'Title ' +  newDict.get("title") + ' already exists, try again.'
    # get list of all snippets for display on view
    snippets = Snippets.objects.all()
    # // reset the form
    form = AddSnippet()
    return render(request, 'index.html', {'form': form, "snippets": snippets, "updateerror": error})

# Main Form View
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        # get list of all snippets for display on view
        snippets = Snippets.objects.all()
        # // reset the form
        form = AddSnippet()
        return render(request, 'index.html', {'form': form, "snippets": snippets, "error": ""})

    def post(self, request, **kwargs):
        form = AddSnippet(request.POST)
        error = ""
        # verify that form is valid
        if form.is_valid():
            # save the form data to database
            try:
                form.save(commit=True)
            except:
               error = 'Title already exists'
            # get list of all snippets for display on view
            snippets = Snippets.objects.all()
            # // reset the form
            form = AddSnippet()
            return render(request, 'index.html', {'form': form, "snippets": snippets, "error": error})



