#!/usr/bin/python

import os
import sys
import time

base = 60
minutes = 25

if len(sys.argv)>1:
	minutes = int(sys.argv[1])

while(minutes>0):
	time.sleep(base)
	minutes-=1
	print(minutes)

os.popen('notify-send -i face-wink "Go" && mplayer /usr/share/sounds/ubuntu/notifications/Blip.ogg').read()
