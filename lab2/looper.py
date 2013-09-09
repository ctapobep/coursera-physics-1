from __future__ import division, print_function
from visual import *
import csv

from common.physutil import *


class Looper:
  def __init__(self, delta_t=0.01):
    self.delta_t = delta_t
    self.trail = curve(color=color.green, radius=0.02)
    self.graph = PhysGraph(1)
    self.time = 0

  def loop(self, ball_sphere, force_vector, duration):
    ball_sphere.vel += (force_vector / ball_sphere.m)*duration
    end_time = self.time + duration
    while self.time < end_time:
      # noinspection PyPropertyAccess
      ball_sphere.pos += ball_sphere.vel * self.delta_t
      self.time += self.delta_t

      self.trail.append(pos=ball_sphere.pos)
      self.graph.plot(self.time, ball_sphere.pos.x)

      #To speed up or slow down program execution
      rate(100)

      self.data_writer.writerow([self.time, ball_sphere.pos.x])


  def open_file(self):
    self.outputfile = open('expected_data.csv', 'w')
    self.data_writer = csv.writer(self.outputfile, delimiter=',', lineterminator='\n', quotechar='|',
                                  quoting=csv.QUOTE_MINIMAL) # Create writer object
    self.data_writer.writerow(['Time (s)', 'Position (m)']) # Write column headers for time, position, and velocity


  def close_file(self):
    self.outputfile.close()