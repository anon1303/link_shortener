from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Link
from .forms import LinkForm

# Create your views here.
def index(request):
    links = Link.objects.all()
    content = {
        'links':links
    }
    return render(request, 'links/index.html', content)

# oursite.com/google -> www.google.com
def root_link(request, link_slug):
    link = get_object_or_404(Link, slug = link_slug)
    # increment the counter to the link
    link.click() #increment the clicked fields

    return redirect(link.url)

def add_link(request):
    if request.method == 'POST':
        #  form has data
        form = LinkForm(request.POST)
        # if the input is valid
        if form.is_valid():
            # save data and return to the homepage
            form.save()
            return redirect(reverse('home'))
    else:        
        form = LinkForm()
    context = {
        "form": form
    }
    return render(request, 'links/create.html', context)