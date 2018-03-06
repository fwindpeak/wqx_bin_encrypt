#!/usr/bin/env python
import sys
import keytab as keytab

def getValue(ch,cv):
    ch = ch & 0xff
    cv = cv & 0xff
    for i in xrange(256):
        if keytab.keytab[ch][i] == cv:
            break
    return i

def xor(t):
      return t[0]^t[1]

def decode(fn):
    fpin = open(fn,'rb')
    jm_len = fpin.read(1)
    jm_len = ord(jm_len)
    randm_pwd = fpin.read(jm_len)
    t = fpin.read(2)
    t = map(ord,t)
    addr = t[0] + t[1]*256+78
    addr2 = addr + jm_len + 3
    fpin.seek(addr2)
    passwd = fpin.read(jm_len)
    a=map(ord,randm_pwd)
    b=map(ord,passwd)
    passwd = map(xor, zip(a,b))
    fpout = open(fn+'.out','wb')
    fpin.seek(jm_len+3)
    dat = fpin.read(addr)
    i=0
    j=0
    while True:
      if j >= addr:
            break
      if i == jm_len:
            i = 0
      value = passwd[i]
      i=i+1
      c = ord(dat[j])
      r = getValue(value,c)
      if j>=78:
            fpout.write(chr(r))
      j=j+1
    j=j+jm_len
    dat=fpin.read(jm_len)
    fpout.write(dat)
    dat = fpin.read()
    j=0
    while True:
          if j>=len(dat)-1:
                break
          if i == jm_len:
                i = 1
          value = passwd[i]
          i=i+1
          c=ord(dat[j])
          j = j+1
          r = getValue(value,c)
          fpout.write(chr(r))
    fpin.close()
    fpout.close()

if __name__ == '__main__':
    decode(sys.argv[1])
