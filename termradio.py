#!/usr/bin/env python3
import os, sys, json, random

# Find lots more stations at http://www.iheard.com
with open('stations.txt') as f:
  txt = f.read()

stations = json.loads(txt)
# PARSING
print('script call format: python radio.py <stationName>, or run without arguments for a random station')
args = sys.argv
if len(args) > 1:     # use radio station library
  station = stations[args[1]]
else:                 # random station
  station = random.choice(list(stations.values()))
print(f"Playing {station}")
# PLAYBACK
# uses https://linux.die.net/man/1/mplayer; can use vlc too
ext = station.split(".")[-1]
if ext in ["pls", "m3u"]: # playlist files
  cmd = f"mplayer -really-quiet -vo none -volume 128 -playlist {station}"
else :                    # bare stream
  cmd = f"mplayer -really-quiet -vo none -volume 128 {station}"
# run - Ctrl + C to exit
while True:
    os.system(cmd)
    user_input = input("Press enter for another random station or press 'e' to quit: ")
    if user_input == "":
        station = random.choice(list(stations.values()))
        ext = station.split(".")[-1]
        if ext in ["pls", "m3u"]: # playlist files
            cmd = f"mplayer -really-quiet -vo none -volume 128 -playlist {station}"
        else :                    # bare stream
            cmd = f"mplayer -really-quiet -vo none -volume 128 {station}"
        print(f"Playing {station}")
    elif user_input == "e":
        break

