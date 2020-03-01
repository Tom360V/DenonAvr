#!/usr/bin/python 


#https://www.google.com/url?sa=t&source=web&rct=j&url=https://usa.denon.com/us/product/hometheater/receivers/avr3808ci%3Fdocname%3DAVR-3808CISerialProtocol_Ver520a.pdf&ved=2ahUKEwjN-aahj_nnAhWOyKQKHbHlBVQQFjABegQIBRAB&usg=AOvVaw2PeekZevgp-p3uxlmW9o3B


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

    def PanelUnlock(self):
        self.Send("SYPANEL LOCK OFF")
        
    def PanelLockFull(self):
        self.Send("SYPANEL+V LOCK ON")

    def PanelLock(self):
        self.Send("SYPANEL LOCK ON")

if __name__== "__main__":
    dc = DenonCommand("192.168.1.30");
    #dc.PowerOn()
    #dc.Up()
    #dc.PowerOff()

    key = ''
    while 'q' != key:
        key = input(">>")
        if 'u' == key:
            dc.PanelUnlock()
        elif 'l' == key:
            dc.PanelLock()
        elif '9' == key:
            dc.Down()
        elif '0' == key:
            dc.Up()
