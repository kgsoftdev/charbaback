from django.shortcuts import render
from django.views.generic.edit import CreateView
from charbamodel.models import Charba
from .forms import CharbaForm



# Create your views here.
def core(request):
    return render(request, 'frontend/index.html')


def list(request):
    data = Charba.objects.all()
    context = {
        'data': data
    }
    return render(request, 'frontend/list.html', context)

def list_detail(request, id):
    detail = Charba.objects.get(id=id)
    context = {
        'detail': detail
    }
    return render(request, 'frontend/detail.html', context)

class CharbaCreateView(CreateView):
    form = CharbaForm
    print("yes")
    model = Charba
    fields = ['type_charba', 'code', 'code_chars', 'description', 'user']
    template_name = 'frontend/create_charba.html'

