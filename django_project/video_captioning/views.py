from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Videos
from .forms import UploadFileForm


def index(request):
    context = {}
    return render(request, 'index.html', context)


def demo(request):
    return render(request, 'demo.html')


@ensure_csrf_cookie
def upload_video(request):
    if request.method != 'POST':
        raise Http404()

    form = UploadFileForm(request.POST, request.FILES)

    if not form.is_valid():
        return HttpResponseBadRequest('The form is NOT valid')

    file = request.FILES['file']
    title = file.name
    content = Videos(title=title, file=file)
    content.save()

    return HttpResponse('Video Uploaded Successfully!!!')
