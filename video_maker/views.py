from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from services.video_creator import create_video
from wsgiref.util import FileWrapper
from . import models
from .forms import TextForm


class VideoTemplateView(CreateView):
    template_name = 'video_maker.html'
    model = models.VideoText
    form_class = TextForm

    def post(self, request, *args, **kwargs):
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            text = form.cleaned_data['text']
            return HttpResponseRedirect(f"{reverse('video_maker')}?text={text}")

    def get(self, request, *args, **kwargs):
        text = request.GET.get('text', '')

        if not text:
            return super().get(request, *args, **kwargs)

        video_name = create_video(text=text)
        video = FileWrapper(open(video_name, 'rb'))
        response = HttpResponse(video, content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename={video_name}'

        text = models.VideoText(text=text)
        text.save()

        fs = FileSystemStorage()
        fs.delete(video_name)

        return response
