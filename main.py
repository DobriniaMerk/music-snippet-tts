import genius, youtube, whisper
import os
import subprocess

remove = True

query = whisper.strip('In a hole in the ground there lived a hobbit').split()
BASE_SEARCH_LEN = 3
SAMPLERATE = 44100
search_len = BASE_SEARCH_LEN

counter = 0
page = 1

while len(query):
    search = ' '.join(query[:search_len])
    print(f'Searching for "{search}"...')
    songs = genius.find_songs_by_snippet(search, 7, page)

    search_len -= 1  # decrement in case nothing will be found

    for song in songs:
        if not song.is_song or search not in whisper.strip(song.download_lyrics()):
            continue

        filename = song.title.replace(' ', '_')
        filepath = os.path.join('downloads', filename)

        print('Downloading:', song.title, '—', song.artist)
        if not youtube.download(song.title + ' - ' + song.artist, filepath):
            print('Too long, skipping.')
            continue

        wordc, start, end = whisper.get_snippet_timestamp(filepath + '.mp3', query)

        if wordc > 0:
            print(
                f'Found {wordc} matching words, starting at {float(start) / 100}ms and ending at {float(end) / 100}ms')
            print('Extracting...')

            subprocess.run(
                f'sox {filepath}.mp3 {counter}.mp3 trim {float(start) / 100} ={float(end) / 100} rate {SAMPLERATE}')
            print('Done.')

            counter += 1
            query = query[wordc:]
            search_len = BASE_SEARCH_LEN  # restore to original length because search terms are changed
            break
        else:
            print('Found no matches')

print('Concatenating...')

subprocess.run('sox ' + ' '.join(f'{i}.mp3' for i in range(counter)) + ' result.mp3')

if remove:
    for i in range(counter):
        os.remove(f'{i}.mp3')

print('Done.')
