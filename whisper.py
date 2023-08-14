import collections

from pywhispercpp.model import Model
from pywhispercpp.constants import AVAILABLE_MODELS
import string

model = Model(AVAILABLE_MODELS[2], n_threads=4, print_realtime=True, print_progress=False)


def transcribe(filepath: string):
    """
    Transcribes audio file and returns timestamps of beginning and ending of every word
    :param filepath: File to transcribe
    :return: List of segment objects, each with start, end, and text fields
    """
    # pprint(model.get_params_schema())
    try:
        segments = model.transcribe(filepath, token_timestamps=True, new_segment_callback=None,
                                    max_len=1, suppress_non_speech_tokens=False, speed_up=False)
    except Exception as e:
        print('Something in Whisper\'s gears has gone terribly wrong, it says:', e)
        segments = []
    return segments


# def new_segment(segments):
#     for segment in segments:
#         print(segment.text, end=' ')
#     print()


def get_snippet_timestamp(filepath: str, snippet):
    """
    Returns starting and ending timestamps (in 1/100`s of a second) for longest snippet match in audiofile
    :param filepath: File to be searched
    :param snippet: Text snippet to search; in form of array of lowercase words
    :return: number of words matched, start, end
    """
    seg_snippet = []
    for piece in snippet:
        seg_snippet.extend(piece.split(' '))
    segments = transcribe(filepath)

    i = 0
    start = end = 0
    match = [-1, -1, -1]
    wordc = 0
    for s in segments:
        text = strip(s.text)

        if len(text) == 0 or s.t1 == s.t0:
            continue

        if i < len(seg_snippet):
            if seg_snippet[i] == text:
                if i == 0:
                    start = s.t0
                i += 1
                end = s.t1
                wordc += 1
            else:
                if wordc > match[0]:
                    match = [wordc, start, end]
                start = end = -1
                wordc = i = 0
        else:
            if wordc > match[0]:
                match = [wordc, start, end]
            start = end = -1
            wordc = i = 0

    return match[0], match[1], match[2]


def strip(s: str):
    """
    Deletes all punctuation and turns all characters lowercase in a string
    """
    return s.translate(str.maketrans('', '', string.punctuation)).lower()
