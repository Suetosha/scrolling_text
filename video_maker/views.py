from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import TemplateView
from services.video_creator import create_video
from wsgiref.util import FileWrapper
from . import models


class VideoTemplateView(TemplateView):
    template_name = 'video_maker.html'

    def get(self, request, *args, **kwargs):
        text = request.GET.get('text', '')

        if not text:
            return HttpResponse("Необходимо передать параметр 'text' в запрос", status=400)

        video_name = create_video(text=text)
        video = FileWrapper(open(video_name, 'rb'))
        response = HttpResponse(video, content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename={video_name}'

        text = models.VideoText(text=text)
        text.save()

        fs = FileSystemStorage()
        fs.delete(video_name)

        return response
