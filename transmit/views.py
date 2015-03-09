from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from django.http import HttpResponse
from transmit.models import Files

import subprocess
from os import listdir
from os.path import isfile, join

# Create your views here. 
'''
   to start a radio transmission, the format is 'pifmplay <dir of file> <freq>
   to edit the freq, edit ~/pifmplay/pifmplay, 'frequency=91.3' is default
   example: sudo sh /home/pi/pifmplay/pifmplay "/home/pi/music/Daft Punk/Technologic.mp3" 91.3
'''

class TransmitView(ListView):
    files = Files.objects.all()
    directory = '/./home/pi/Music'
    dir_files = [f for f in listdir(directory) if isfile(join(directory,f))]
	
    #add any new files to Files model
    for file in dir_files:
        if file in files:
            pass
	else:
	    thisFile = Files.objects.create(file_name=file, file_path=join(directory,file), times_played=0)
	    thisFile.save()

    #Remove any files from Files model that no longer exist
    for file in files:
        if file in dir_files:
            pass
	else:
	    file.delete()
	    
    
    #return model for list view rendering
    model = Files
    context_object_name = 'files'

class Player(View):
    def get(self, request):
	if request.method == 'GET':
	    action = request.GET.get('action')

	    #play will be sent in the URI for a new file play
	    if action == 'play':
	        thisFile = request.GET.get('file_path')
	        mediaFile = Files.objects.get(file_name=thisFile)
	        mediaFile.times_played += 1
	        mediaFile.save()
	        command = 'sudo sh /home/pi/pifmplay/pifmplay', thisPath
 
	    #pause will be sent if pausing a currently playing file
	    elif action == 'pause':
		command = 'sudo sh /home/pi/pifmplay/pifmplay', 'pause', '&>/dev/null &'
	    #resume will be sent if resuming a currently paused file
	    elif action == 'resume':
		command = 'sudo sh /home/pi/pifmplay/pifmplay','resume', '&>/dev/null &'

	    #stop a currently playing file
	    elif action == 'stop':
		command = 'sudo sh /home/pi/pifmplay/pifmplay','stop','&>dev/null &'	    

	    subp = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	    output = subp.communicate()[0]
	    
	    return HttpResponse('action taken was ', action)
	else:
	    return HttpResponse('error transmitting')	





