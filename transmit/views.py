from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View, DetailView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.servers.basehttp import FileWrapper
from transmit.models import Files
import subprocess
import os
import fnmatch


'''
	This file is used to manage the music interface.
        beets is used to organize music, get metadata, and web player interface
        configure beets directory with beet config -e
            directory: ~/beets-music
            library: ~/data/musiclibrary.blb
        #run $ beet import /home/matthew/Music periodically to import and sort new music ( $ beet import -A /home/matthew/Music for fast noninteractive)
'''

musicPath = "/home/matthew/carpi/transmit/media/beets-music/"

class TransmitView(DetailView):

    model = Files

    def get_context_data(self, **kwargs):
        context = super(TransmitView, self).get_context_data(**kwargs)
        context['songs'] = Files.objects.all()
        return context

    def get_object(self):
        pass

class Player(View):
    def get_context_data(self, **kwargs):
        context = super(Player, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        song = Files.objects.get(id = self.kwargs['id'])
        #incriment the play_count attribute and save the new data
        song.times_played += 1
        song.save()

        wrapper = FileWrapper(file(song.file_path))
        response = HttpResponse(wrapper, mimetype='audio/mpeg')
        response['Content-Length'] = os.path.getsize(song.file_path)
        response['Content-Disposition'] = 'filename=%s' % song.file_name
        return response

class RefreshMedia(View):

    #csrf_exempt decorator only works on the dispatch method
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(RefreshMedia, self).dispatch(*args, **kwargs)
    
    def post(self, request):
        if request.method == 'POST':
            #refresh the database files list
            # remove files no longer present
            for file in Files.objects.all():
                if file not in musicPath:
                    file.delete()
            
            #add files that aren't currently in the database
            for root, dirnames, filenames in os.walk(musicPath):
                for filename in filenames:
                    if filename not in [f.file_name for f in Files.objects.all()]:
                        Files.objects.create(file_name = filename, file_path = os.path.join(root, filename), times_played = 0)
            return HttpResponse('Music Database Refreshed!')
        else:
            return HttpResponse('must access through post')







