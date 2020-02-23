#!/usr/bin/python

import socket
import sys
import os
from time import sleep


class DenonCommand:
    CR = "".join(map(chr,[13]))
    def __init__(self, receiverIp):
        self.receiverIp = receiverIp
        print("Init " + self.receiverIp)
        self.port = 23
        
    def Send(self, cmd):
        print("Request: " + cmd)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        try:
            s.connect((self.receiverIp, self.port))
            s.send(bytearray(cmd + '\r', 'ascii'))
            r = s.recv(135)
            print("response: " + str(r))
            s.close()
            sleep(0.06)
            return #ant
        except socket.error as e:
            print("Socket verbinding error:" + str(e))
        return
        
    def PowerOn(self):
        self.Send("PWON")
    def PowerOff(self):
        self.Send("PWSTANDBY")
    def Power(self):
        self.Send("PW?")

    def Up(self):
        self.Send("MVUP")
    def Down(self):
        self.Send("MVDOWN")
    def VolumeSet(self, db):
        self.Send("MV"+str(db))

    def NSA(self):
        self.Send("NSA")
        self.Send("NSE")

if __name__== "__main__":
    dc = DenonCommand("192.168.1.30");
    #dc.PowerOn()
    dc.Up()
    #dc.PowerOff()
