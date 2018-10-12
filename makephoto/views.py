from django.shortcuts import render, get_object_or_404, render_to_response
from .forms import PhotoForm
from .models import PhotoModel
from django.http import HttpResponseRedirect, HttpResponse


def view_photo(request, slug):
    photo = get_object_or_404(PhotoModel, pk=slug)
    return render(request, 'view_photo.html', {'photo': photo})


def take_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            url = photo.get_url()
            return HttpResponseRedirect(url)
    else:
        form = PhotoForm()
    return render(
        request,
        'take_photo.html',
        {'form': form},
    )
