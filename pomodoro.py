#!/usr/bin/python

import os
import sys
import time
import signal

# Manage CTRL-C signal
def signal_handler(signal, frame):
	print('Stopping pomodoro!')
	sys.exit(0)


# Install signal handler
signal.signal(signal.SIGINT, signal_handler)

base = 60
minutes = 25

if len(sys.argv)>1:
	minutes = int(sys.argv[1])

os.popen('notify-send -i face-wink "Start" && mplayer /usr/share/sounds/ubuntu/notifications/Blip.ogg').read()

while(minutes>0):
	minutes-=1
	print(minutes)
	time.sleep(base)

os.popen('notify-send -i face-wink "Go" && mplayer /usr/share/sounds/ubuntu/notifications/Blip.ogg').read()
