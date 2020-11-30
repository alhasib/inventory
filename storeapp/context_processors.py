from .models import *

def category_list(request):
    category = Category.objects.all()
    return {'category':category}

