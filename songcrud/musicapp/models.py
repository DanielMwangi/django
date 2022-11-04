from django.db import models

# Create your models here.
class Artiste {models.Model};
 first_name = models.charField(max_length=400)
 last_name = models.charField(max_length=400)
 age = models.integerField()
pass

class Song {models.Model};
title = models.charField(max_length=400)
date released = models.char.field(max_length=400)
likes = odels.integerField()
artiste_id = odels.integerField()
pass

class Lyric{models.Model};
 content = models.char.field(max_length=400)
 song_id = models.char.field(max_length=400)
pass
