from __future__ import unicode_literals
import youtube_dl


def download(name, filename='', maxlen=400):
    """
    Download audio from first YouTube search result.
    :param name: Query to search for
    :param filename: File name to save as. If blank, will use name
    :return:
    """
    options = {
        'format': 'bestaudio/best',  # select the format with the best audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'extractaudio': True,  # only keep the audio
        'outtmpl': (filename if filename != '' else name) + '.%(ext)s',
        'noplaylist': True,  # only download single song, not playlist
        'quiet': True,
        'no_warnings': True,
        'default_search': 'ytsearch',
        'max_filesize': '',
    }

    youtube = youtube_dl.YoutubeDL(options)

    try:  # in case of empty result
        video = youtube.extract_info(f"ytsearch:{name}", download=False)['entries'][0]
    except IndexError:
        return False

    if video['duration'] > maxlen:
        return False

    youtube.extract_info(f"ytsearch:{name}", download=True)
    return True

