from .models import Category,pages

def global_data(request):
    data={
        'globalData': Category.objects.all(),
        'pageData': pages.objects.all()
    }
    return data