# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
from yandex_music import Client

load_dotenv()

MY_TOKEN_YM = os.environ.get('TOKEN_YM')
MY_ALBUM_ID = os.getenv('ALBUM_ID')


client = Client(MY_TOKEN_YM).init()


album = client.albums_with_tracks(MY_ALBUM_ID)
tracks = []


text = 'АЛЬБОМ\n\n'
text += f'{album.title}\n'
text += f"Исполнитель: {'& '.join([artist.name for artist in album.artists])}\n"
text += f'{album.year} · {album.genre}\n'

text += f'\nТреки альбома {album.title}:\n'

print(text)


for i, volume in enumerate(album.volumes):
    if len(album.volumes) > 1:
        tracks.append(f'{i}')
    tracks += volume


for track in tracks:
    if isinstance(track, str):
        print(track)
    else:
        artists = ''
        if track.artists:
            item = f"{track.title} - {' & '.join([artist.name for artist in track.artists])}"
        print(item)
