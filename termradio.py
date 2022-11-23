#!/usr/bin/env python3

# %%
import os, sys, json

# Find lots more stations at http://www.iheard.com
with open('stations.txt') as f:
  txt = f.read()

stations = json.loads(txt)
# %% PARSING
print('script call format: python radio.py <stationName>')
if "://" in sys.argv[1]: # interpret this as a radio station URL
  station = sys.argv[1]
else:                # use radio station library
  station = stations[sys.argv[1]]

print(f"Selected station URL is {station}")

# %% PLAYBACK
# uses https://linux.die.net/man/1/mplayer; can use vlc too
ext = station.split(".")[-1]
if ext in ["pls", "m3u"]: # playlist files
  cmd = f"mplayer -really-quiet -vo none -volume 128 -playlist {station}"
else :                    # bare stream
  cmd = f"mplayer -really-quiet -vo none -volume 128 {station}"
# run - Ctrl + C to exit
os.system(cmd)
# %%
