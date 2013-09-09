# STARTUP (Don't edit, typically) 
from __future__ import division, print_function
from visual import *
import csv

from common.physutil import *
from looper import Looper

SYSTEM_MASS = 1.5
SYSTEM_POSITION = vector(0, 0, 0)
SYSTEM_INITIAL_VELOCITY = vector(5, 0, 0)
SYSTEM_INITIAL_POSITION = vector(0, 0, 0)
DELTA_T = 0.003

# Setup Display window for visualization
scene = display(width=640, height=480, background=color.white, range=2.5, title="VPython Test")
# Create object for visualization
ball = sphere(color=color.blue, radius=0.10)
# Create a track behind object to visualize trajectory
trail = curve(color=color.green, radius=0.02)
# Create small sphere to mark the origin in Display window
origin = sphere(pos=SYSTEM_POSITION, color=color.yellow, radius=0.04)

ball.m = SYSTEM_MASS

# noinspection PyPropertyAccess
ball.pos = SYSTEM_INITIAL_POSITION
ball.vel = SYSTEM_INITIAL_VELOCITY

looper = Looper(delta_t=DELTA_T)
looper.open_file()
looper.loop(ball, vector(0, 0, 0), .867)
looper.loop(ball, vector(-18.1,0,0), .074)
looper.loop(ball, vector(0,0,0), .634)
looper.close_file()



