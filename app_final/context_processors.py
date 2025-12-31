from app_final.models import category

def get_categories(request):
    categories=category.objects.all()
    data={
        'categories':categories
    }
    return data

