from django.shortcuts import render
from puntos.forms import PersonForm
from puntos.models import Person, RolProfesional

# Create your views here.
def index(request):
    return render(request, 'puntos/index.html', {})

def person_view(request):
    if request.method == 'POST':
        form= PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form= PersonForm
    return rednder(request, 'puntos/puntos_form.html', {'form': form})
