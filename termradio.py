#!/usr/bin/env python3

# %%
import os, sys, json, random, shutil, subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f'{script_dir}/stations.txt') as f:
  txt = f.read()

stations = json.loads(txt)
# %% PARSING
print('script call format: python radio.py <stationName>')
if len(sys.argv) > 1:
    station_name = sys.argv[1]
    if "://" in station_name: # interpret this as a radio station URL
      station_url = station_name
    else:                # use radio station library
      try:
        station_url = stations[station_name]
      except KeyError:
        print(f"Station '{station_name}' not found in stations.txt.")
        print("Available stations are:")
        for s in stations:
            print(f"- {s}")
        sys.exit(1)
else: # play random station
    station_name, station_url = random.choice(list(stations.items()))
    print(f"No station specified, playing a random one: {station_name}")

print(f"Selected station URL is {station_url}")

# %% PLAYBACK
def find_player():
    """Finds an available command-line audio player."""
    for player in ["mpv", "mplayer", "vlc"]:
        if shutil.which(player):
            return player
    return None

player = find_player()

if not player:
    print("No supported player (mpv, mplayer, vlc) found.")
    print("Please install one of them to play radio streams.")
    sys.exit(1)

print(f"Using {player} for playback.")

ext = station_url.split(".")[-1]

cmd = [player]
if player in ["mpv", "mplayer"]:
    if ext in ["pls", "m3u"]:
        cmd.extend(["-playlist", station_url])
    else:
        cmd.append(station_url)
elif player == "vlc":
    cmd.extend(["--no-video", station_url])

# run - Ctrl + C to exit
try:
    # For VLC, you might want to suppress the verbose output
    extra_args = {}
    if player == "vlc":
        extra_args = {"stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
    subprocess.run(cmd, **extra_args)
except KeyboardInterrupt:
    print("\nExiting.")
# %%
