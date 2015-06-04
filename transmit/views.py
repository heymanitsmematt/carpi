from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View, DetailView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.servers.basehttp import FileWrapper
from transmit.models import Files, Artist, Song, Album
import subprocess
import shlex
import os
import fnmatch

#debug only
import sys
import pdb

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
                if file not in os.walk(musicPath):
                    file.delete()
            try:    
                #add files that aren't currently in the database
                for root, dirnames, filenames in os.walk(musicPath):
                    for filename in filenames:
                        if filename not in [f.file_name for f in Files.objects.all()]:
                            Files.objects.create(file_name = filename, file_path = os.path.join(root, filename), times_played = 0)
                
                #deep datatabse encoding for files. get list of files, parse, and save
                args = shlex.split('beet list')
                proc = subprocess.Popen(args, stdout=subprocess.PIPE)
                rawData = proc.stdout.read().replace('\n',',').split(',')
                rawData.pop()

                # split and save artist, album, track into database, adding fk values
                for aatGroup in rawData:
                    #add those that do match the obvious artist-album-track format
                    chunk = aatGroup.split('-')
                    thisArtist = Artist.objects.get_or_create(artist_name=chunk[0])[0]
                    thisAlbum = Album.objects.get_or_create(album_name=chunk[1], artist_fk = thisArtist)[0]
                    thisTrack = Song.objects.get_or_create(song_name=chunk[2], album_fk = thisAlbum)[0]

                    try:
                        thisTrack.files_fk = Files.objects.get(file_name__contains = thisTrack.song_name)
                    except:
                        err = sys.exc_info()
                        pdb.set_trace()

                    thisArtist.save()
                    thisAlbum.save()
                    thisTrack.save()

                return HttpResponse('Music Database Refreshed!')
            except: 
                err = sys.exc_info()
                pdb.set_trace()
        else:
            return HttpResponse('must access through post')







