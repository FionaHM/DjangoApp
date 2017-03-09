from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Snippets
from .forms import AddSnippet
from .forms import EditSnippet
from django.views.generic.edit import UpdateView

def delete_item(request, pk):
    # get item
    print(" in here")
    post = Snippets.objects.get(pk = pk)
    # delete it
    post.delete()
    snippets = Snippets.objects.all()
    form = AddSnippet()
    return render(request, 'index.html', {'form': form, "snippets": snippets})

def edit_item(request, pk):
    # get item
    item = Snippets.objects.get(pk = pk)
    snippets = Snippets.objects.all()
    form = AddSnippet()
    edititem = EditSnippet(instance=item)
    return render(request, 'index.html', {'form': form, "snippets": snippets, 'edititem': edititem})

# Update View
class ItemUpdate(UpdateView):
    model = Snippets
    fields = ['title']
    template_name_suffix = '_update_form'

def update_item(request):
    # verify that form is valid

    if request.method == 'POST':
        form = EditSnippet(request.POST)
        title = form['title'].value()
        # ItemToUpdate = Snippets.objects.select_for_update().filter(title=title)
        language = form['language'].value()
        snippet = form['snippet'].value()
        description = form['description'].value()
        print (title)
        Snippets.objects.select_for_update().filter(title=title).update(language = language)
        Snippets.objects.select_for_update().filter(title=title).update(snippet = snippet)
        Snippets.objects.select_for_update().filter(title=title).update(description = description)
    try:
        snippets = Snippets.objects.all()
    except Snippets.DoesNotExist:
        raise Http404("Snippets does not exist")
    # // reset the form
    form = AddSnippet()
    return render(request, 'index.html', {'form': form, "snippets": snippets})

# Main Form View
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        form = AddSnippet()
        try:
            snippets = Snippets.objects.all()
        except Snippets.DoesNotExist:
            raise Http404("Snippets does not exist")
        return render(request, 'index.html', {'form': form, "snippets": snippets})

    def post(self, request, **kwargs):
        form = AddSnippet(request.POST)
        # verify that form is valid
        if form.is_valid():
            # save the form data to database
            try:
                form.save(commit=True)
            except:
                print("object already exists")

            try:
                snippets = Snippets.objects.all()
            except Snippets.DoesNotExist:
                snippets = ""
                print("empty object")
            # // reset the form
            form = AddSnippet()
            return render(request, 'index.html', {'form': form, "snippets": snippets})



