#!/usr/bin/python
# -*- coding: utf-8 -*-
"""gpsserver.py: routes gps messages from serial/usb GPS device, e.g. /dev/ttyACMx to network port tcp server ."""

__author__      = "Henrik Schulz"
__copyright__   = "Copyright 2019, for the QMS project"
__license__     = "GPL"

# gpsserver.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gpsserver.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# see <http://www.gnu.org/licenses/>.
try:
    import SocketServer
except ImportError:
    import socketserver as SocketServer

import re
import os
import sys
import argparse
import serial
import time

port=10000
hostname='localhost'

gpsSerialDevice="ttyACM"
gpsSerialDevicePattern=gpsSerialDevice+r'[0-9]+'
gpsSerialDeviceDirectory="/dev/"

class GPSTCPServer(SocketServer.TCPServer):
    def __init__(self,server,handler):
        SocketServer.TCPServer.__init__(self,server,handler)
 
    def connectGPSSerialDevice(self,deviceDirectory,devicePattern):
        self.deviceDirectory=deviceDirectory
        self.devicePattern=devicePattern
        gpsSerialDevices = self.findSerialPortConnectedToGps(deviceDirectory,devicePattern)
        if len(gpsSerialDevices) == 0:
            print ("Wait until GPS serial device is connected")
        while len(gpsSerialDevices) == 0:
            time.sleep(5) 
            gpsSerialDevices = self.findSerialPortConnectedToGps(deviceDirectory,devicePattern)
           
        self.gpsdev = gpsSerialDevices[0]   

        if os.path.exists(self.gpsdev):
            try:
                print ("Opening GPS serial device '{}'".format(self.gpsdev) )
                self.gpsdevfile = serial.Serial(self.gpsdev, 9600)
            except RuntimeError:
                print ("ERROR: runtime error opening : " + self.gpsdev + " (perhaps device or resource busy, i.e. it may conflict with gpsd - thus set USBAUTO=no in /etc/default/gpsd)")
              
    def reconnectGPSSerialDevice(self):
        print ("Reconnect GPS serial device '{}'".format(self.gpsdev) )
        self.connectGPSSerialDevice(self.deviceDirectory,self.devicePattern)
              

    def findSerialPortConnectedToGps(self,deviceDirectory,devicePattern):
        files=list()
        for f in [f for f in os.listdir(deviceDirectory) if re.match(devicePattern, f)]:
            files.append(os.path.join(deviceDirectory,f))
        return files 

    def __del__(self):
        if hasattr(self,'gpsdevfile'):
           if self.gpsdevfile.isOpen():
              print ("Closing GPS serial device {}".format(self.gpsdev) )
              self.gpsdevfile.close()

class GPSTCPServerHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print ("Starting to route GPS data from serial device '{}'".format(self.server.gpsdev) )
        if self.server.gpsdevfile.isOpen():
            gpsdata=False
            while not gpsdata: 
                try:
                    gpsdata = self.server.gpsdevfile.readline()
                except serial.SerialException:
                    print ("Reading from GPS serial device '{}' interrupted".format(self.server.gpsdev) )
                    self.server.gpsdevfile.close()

                    self.server.reconnectGPSSerialDevice()
                except KeyboardInterrupt:
                    print ("Reading from GPS serial device '{}' interrupted".format(self.server.gpsdev) )
                    return
                                       
            while ( gpsdata ):
                try:  
                    self.wfile.write(gpsdata)
                except:
                    return 
                gpsdata=False
                while not gpsdata: 
                    try:
                        gpsdata = self.server.gpsdevfile.readline()
                    except serial.SerialException:
                        print ("Reading from GPS serial device '{}' interrupted".format(self.server.gpsdev) )           
                        self.server.gpsdevfile.close()

                        self.server.reconnectGPSSerialDevice()
                    except KeyboardInterrupt:
                        print ("^C received, reading from GPS serial device '{}' interrupted".format(self.server.gpsdev) )
                        return
                        
    def finish(self):
        print ("Reading from GPS serial device '{}' interrupted".format(self.server.gpsdev) )
        pass
          
parser = argparse.ArgumentParser()
parser.add_argument("--port", help="provide port to listen at, default=10000", type=int, default=port)
parser.add_argument("--host", help="provide host name to listen, default=localhost", default=hostname)
parser.add_argument("--device", help="provide device pattern, e.g. ttyACM without number, default=ttyACM", default=gpsSerialDevice)
parser.add_argument("--device-directory", help="provide device directory, e.g. /dev, default=/dev", default=gpsSerialDeviceDirectory)

args = parser.parse_args()
   
port = args.port   
hostname = args.host

gpsSerialDeviceDirectory = args.device_directory
gpsSerialDevicePattern=gpsSerialDevice+r'[0-9]+'


try:            
    print ("Started gps-server on {}:{} reading from devices '{}'".format(hostname, port,os.path.join(gpsSerialDeviceDirectory,gpsSerialDevicePattern) ) )

    GPSTCPServer.allow_reuse_address = True
    server = GPSTCPServer((hostname, port), GPSTCPServerHandler)

    server.connectGPSSerialDevice(gpsSerialDeviceDirectory,gpsSerialDevicePattern)

    server.serve_forever()

except KeyboardInterrupt:
    print ("^C received, shutting down the GPS TCP server")
    server.server_close()
except  Exception as msg:
    print ("Couldn't connect with the socket-server: '{}' ... terminating program".format(msg))
    server.server_close()
