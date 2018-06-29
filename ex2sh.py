#!/usr/bin/python

import sys
import re

class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

ops = ""

try:
  while True:
    line = sys.stdin.readline()
    if line:
      if re.match("^[ ]*[0-9a-f]*:.*$",line):
        line =line.split(":")[1].lstrip()
        om = line.split("\t")
        op = re.findall("[0-9a-f][0-9a-f]",om[0])
        for i in op:
          ops += "\\x%s" % i
    else:break
  print bcolors.OKGREEN + "\"" + ops + "\"" + bcolors.ENDC
except: pass
