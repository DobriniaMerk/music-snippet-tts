# music-snippet-tts

Why have i made this? I don't know. 

Why i am publishing sources? I have no idea, maybe someone will find this intresting.

Does this thing has any practical use? Most probably not.

That's it.

## Installing and usage
<sup>I anyone would want to try this</sup>

To install, you should get yourself an Genius API key, clone this repository, install dependecies from `requirements.txt` and install SoX

```
# Clone this repo
git clone https://github.com/DobriniaMerk/music-snippet-tts.git

# Install dependecies
pip install -r requirements.txt

# Install SoX
sudo apt install sox # on linux
```
On Windows, to install SoX you sould download it from [Sourceforge](https://sourceforge.net/projects/sox/files/sox/) and add to PATH.

Also ffmpeg needed for pywhispercpp to work. Installation process for it left as an excercise for the reader. <sub><sup>i'm too tired to search for it</sup></sub>

After all this, you should get yoursef a Genius API token and put it in the `genius.py`.

That's it.

## Description

This is some strange type of TTS (text to speech) algorithm i accidentally thought of and decided to make.
Instead of generating audio with neural networks or synthesyzing it with some complex algorithms,
this program makes speech by combining together pieces of random songs which contain needed words.
Resulting audio is not very understandable, though.

That's it.

## Realization

First things first, you need to find from which songs to steal the words.
Here it is done with use of [Genius](https://genius.com/), one of the biggest lyrics database.
As i haven't wanted to do everything by hand with requests and so on,
i used the [LyricsGenius](https://github.com/johnwmillr/LyricsGenius#usage) Python library,
one of good thing about it, is that it can download full lyrics for the song, feature that is strangely not in the Genius API.

Then, after the songs are found, i download their audio from [YouTube](youtube.com),
with the [youtube-dl](https://github.com/ytdl-org/youtube-dl#embedding-youtube-dl).

Downloaded song than are transcribed with Whisper AI model, to find where in the treck are desired words.
To make things faster (but still not fast enough on my machine) i used [whisper.cpp](https://github.com/ggerganov/whisper.cpp) Python wrapper: [pywhispercpp](https://github.com/abdeladim-s/pywhispercpp/tree/main)

And finaly the audio is cut and combined by [SoX](https://sox.sourceforge.net/sox.html), audio processing command line multitool.

That's it.

<sub><sup>I spent too much time on this thing.</sup></sub>
