#!/usr/bin/env python
# coding: utf-8


import pynmea2     # install with "pip install pynmea2"
import time
import sys

def DataConverterAndWriter(lne):
    msg = pynmea2.parse(lne)
    idx = msg.name_to_idx
    msg.data[idx["gps_qual"]] = '1'
    msg.data[idx["timestamp"]] = "%s.00" % msg.data[idx["timestamp"]][:6]
    msg = pynmea2.GGA('GP', 'GGA', msg.data)
    
    sys.stdout.write(str(msg)+"\n")
    sys.stdout.flush()
    time.sleep(2)
    
    return

while 1:
  lne = sys.stdin.readline()
  if len(lne) < 2:
    break
    
  DataConverterAndWriter(lne)  
  





