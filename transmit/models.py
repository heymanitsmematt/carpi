from django.db import models

class Files(models.Model):
    file_name = models.CharField(max_length=300)
    file_path = models.CharField(max_length=300)
    times_played = models.IntegerField(null=True)

    def __unicode__(self):
        return self.file_name

class Artist(models.Model):
    artist_name = models.CharField(max_length=300)

    def __unicode__(self):
        return self.artist_name

class Album(models.Model):
    album_name = models.CharField(max_length=300)
    artist_fk = models.ForeignKey(Artist, null=True)

    def __unicode__(self):

        return self.album_name
class Song(models.Model):
    song_name = models.CharField(max_length=300)
    album_fk = models.ForeignKey(Album, null=True)
    files_fk = models.ForeignKey(Files, null=True)

    def __unicode__(self):
        return self.song_name


