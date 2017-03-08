from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Snippets


from .forms import AddSnippet

# Create your views here.
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
            form.save(commit=True)
            try:
                snippets = Snippets.objects.all()
            except Snippets.DoesNotExist:
                raise Http404("Snippets does not exist")
            return render(request, 'index.html', {'form': form, "snippets": snippets})



