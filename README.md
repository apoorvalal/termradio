# `termradio` : listen to the radio from the terminal

Lots of radio stations have streaming links that can be piped directly
into a media player. Keeping track of them and playing them in a
browser became cumbersome, so I wrote a little python program
`termradio` to play the radio from the terminal.

Tested on linux.

## usage

```{python}
python3 termradio.py SOMAGroove
```

If you make the script executable [`chmod +x termradio.py`], you can drop the extension and run

```
./termradio KEXP
```

`termradio` accepts 1 argument, which is either a station name in
`stations.txt`, or a streaming url. If you intend to use stations repeatedly.

Stations live in a dictionary `stations.txt`, which is
pre-populated with a few stations I like (KEXP, KCRW, SOMAFM), and can
be added to by the user (please maintain valid python dict syntax).

## media player

Python is currently used purely for argument parsing and storage.
Playback is handled by [mplayer](https://linux.die.net/man/1/mplayer),
which is available for most linux distros [including on windows via
WSL]. It is also available on mac via homebrew
(https://formulae.brew.sh/formula/mplayer, ymmv). 
