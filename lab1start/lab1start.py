# STARTUP (Don't edit, typically) 
from __future__ import division, print_function
from visual import *
import csv

from physutil import *


# VISUALIZATION & GRAPH INITIALIZATION
# ===========================================

# Setup window for plotting
graph = PhysGraph(1)
# Setup Display window for visualization 
scene = display(width=640, height=480, background=color.white, range=2.5, title="VPython Test")
# Create object for visualization
ball = sphere(color=color.blue, radius=0.22)
# Create a track behind object to visualize trajectory
trail = curve(color=color.green, radius=0.02)
# Create small sphere to mark the origin in Display window
origin = sphere(pos=vector(0, 0, 0), color=color.yellow, radius=0.04)


# SYSTEM PROPERTIES and INITIAL CONDITIONS 
# ===========================================

# System Mass
#EDIT THIS (next one line): 
ball.m = 1

#Initial Conditions
#EDIT THIS (next three lines, as necessary) 
ball.pos = vector(0.011, 0, 0)
ball.vel = vector(-0.7879, 0, 0)
t = 0  #the time when we choose to start our clock


# OTHER INITIALIZATION 
# ===========================================
#
#Timestep
#EDIT THIS (next one line, as necessary)
deltat = 0.01

#OPTIONAL: Output model predictions to file (.csv format)
#To use, uncomment next five lines (delete leftmost # ONLY)
outputfile = open('pythonTest.csv', 'w') # Set name of output file.
                                       # NOTE: if the file already exists,
                                        # it will be overwritten
DataWriter = csv.writer(outputfile, delimiter=',', lineterminator='\n',quotechar='|', quoting=csv.QUOTE_MINIMAL) # Create writer object
DataWriter.writerow(['Time (s)','Position (m)']) # Write column headers for time, position, and velocity


# CALCULATION LOOP(Motion Prediction and Visualization)
# ===========================================
while t < 1.734:
  Fnet = vector(0, 0, 0)
  ball.vel += (Fnet / ball.m) * deltat
  ball.pos += ball.vel * deltat
  t = t + deltat

  trail.append(pos=ball.pos)
  graph.plot(t, ball.pos.x)

  #To speed up or slow down program execution
  rate(100)

  DataWriter.writerow([t,ball.pos.x])

print(t, ball.pos.x)

outputfile.close()
