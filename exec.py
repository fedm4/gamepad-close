#!/usr/bin/python
# -*- coding: utf-8 -*-
import inputs
from subprocess import Popen
import sys

flag = True
btnStatus = {}
btnStatus['BTN_SELECT'] = 0
btnStatus['BTN_THUMBL'] = 0
args = sys.argv[1:]
app = Popen(args)
while flag:
    events = inputs.get_gamepad()
    for event in events:
        if event.ev_type == 'Key' and \
			(event.code == 'BTN_SELECT' or event.code == 'BTN_THUMBL'):
            btnStatus[event.code] = event.state
            if btnStatus['BTN_SELECT'] == 1 and btnStatus['BTN_THUMBL'] \
				== 1:
                flag = False
app.terminate()
print('End')
