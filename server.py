# -*- coding: utf-8 -*-
#/usr/bin/python

"""

"""
 
import socket
import threading
import sys
 
#inString = ''
#outString = ''
#nick = ''

# def DealOut(s):
#     global nick, outString
#     while True:
#         outString = raw_input()
#         outString = nick + ': ' + outString
#         s.send(outString)
 
# def DealIn(s):
#     global inString
#     while True:
#         try:
#             inString = s.recv(1024)
#             if not inString:
#                 break
#             if outString != inString:
#                 print inString
#         except:
#             break
def clientThreadIn(conn, nick):
    global data
    while True:
        try:
            tmp = conn.recv(1024)
            if not tmp:
                conn.close()
                return
            #print inString
            NotifyAll(tmp)
            print data    
            #if outString != inString:
            #    print inString
        except:
            NotifyAll(nick+" leave the room!")
            print data
            return
def clientThreadOut(conn, nick):
    global data
    while True:
        if con.acquire():
            con.wait()
            if data:
                try:
                    conn.send(data)
                    con.release()
                except:
                    con.release()
                    return 
def NotifyAll(msg):
    global data
    if con.acquire():
        data = msg
        con.notifyAll()
        con.release()  

con = threading.Condition() 
#nick = raw_input("input your nickname: ")
#ip = raw_input("input the server's ip adrress: ")
ip = '192.168.43.87'
data = ''
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print "Socket has been created"
sock.bind(ip)
#sock.send(nick)
sock.listen(10)
print "Socket is listening now "

while 1:
    conn, addr = sock.accept()
    #print "Connected with"+addr[0]+':'+str(addr[1])
    print str(addr)
    nick = conn.recv(1024)
    NotifyAll('Welcome '+ nick + 'to the room!')
    print data
    print str((threading.activeCount()+1)/2) + 'person(s)!'
    conn.send(data)
    threading.Thread(target = clientThreadIn, args =(conn, nick)).start()
    threading.Thread(target = clientThreadOut, args =(conn, nick)).start()
sock.close()
    