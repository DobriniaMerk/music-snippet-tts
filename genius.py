import lyricsgenius
import string

genius = lyricsgenius.Genius("YOUR TOKEN HERE")
genius.skip_non_songs = True


def search_by_text(snippet: str, num: int, page: int):
    """
    Searches Genius's base of lyrics for a text match with snippet
    :param page:
    :param snippet:
    :param num: Number of results to return
    :return: json structure of results
    """

    search = genius.search_lyrics(snippet, per_page=num, page=page)
    return search


def find_songs_by_snippet(snippet: str, num=5, page=1):
    """
    Searches Genius's base of lyrics for songs whose lyrics contain the snippet
    :param page: Search page number
    :param snippet: Snippet to search
    :param num: Number of songs to return
    :return: list of song objects
    """
    search = search_by_text(snippet, num, page)
    results = [Song(song['result']) for song in search['sections'][0]['hits']]
    return results


class Song:
    """
    Stores info about single song, including artist, title, and full lyrics
    """
    def __init__(self, data):
        self.is_song = data['_type'] == 'song'
        self.title = data['title']
        self.title_with_featured = data['title_with_featured']
        self.artist = data['primary_artist']['name']

    def download_lyrics(self):
        try:
            self.lyrics = genius.search_song(self.title, self.artist).lyrics. \
                translate(str.maketrans('', '', string.punctuation)).lower()
        except:
            self.lyrics = ''
        return self.lyrics
