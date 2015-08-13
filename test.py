#!/usr/bin/env python

import os
import json

dat=json.load(open('banksecurity.json'))

for i in dat.keys():
    os.mkdir (dat[i]['bankName'].lower().replace(' ',''))

print "done"
