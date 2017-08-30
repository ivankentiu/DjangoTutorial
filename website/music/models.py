from django.db import models


# django auto create id behind the scenes Models or Blueprint
# each variable is a column

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    # string representation of object - instead of showing <Album: Album object>.. display title and artist instead

    def __str__(self):
        return self.album_title + ' - ' + self.artist


# each Song needs to be link to an Album / on delete all songs link to the album deleted as well

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title

