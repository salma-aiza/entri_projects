from . models import category

def my_links(request):
    links = category.objects.all()
    return dict(links=links)
