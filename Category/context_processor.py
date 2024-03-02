from .models import * 

def menu_links(request):
    maxsulot_turi = Category.objects.all()
    context = {
        "maxsulot_all" : maxsulot_turi
    }
    
    return context