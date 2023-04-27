from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from wagtail.core.models import Page


def home(request):
    blog_index_page = Page.objects.get(
        slug="blog-index"
    )  # slug de la pagina de indice de blog
    return render(request, "home_page.html", {"blog_index_page": blog_index_page})
