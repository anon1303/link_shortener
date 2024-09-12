from django.shortcuts import render, get_object_or_404

from .models import Link


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