#!/bin/env python3
from fysom import *
import yaml
import random
import time

# import generate_fsm
# endstates = ['C', 'AB', 'XYZ']
endstates = ['C', 'AB', 'LMNOP', 'XYZ']
# trans = ['A', 'B', 'C', 'X', 'Y', 'Z']
trans = ['A', 'B', 'C', 'L', 'M', 'N', 'O', 'P', 'X', 'Y', 'Z']
actions = ['alert', 'clear' ]
# input = ['A', 'B', 'C', 'L', 'M', 'N', 'O', 'P', 'X', 'Y', 'Z']
# endstates = ['C', 'AB', 'LMNOP', 'XYZ']
events = {}
with open("alerts.yaml", 'r') as stream:
    try:
        events = yaml.load(stream)
    except yaml.YAMLError as ex:
        print(ex)
        exit(1)

#print(events)

def printstatechange(e):
    print ('event: %s, src: %s, dst: %s' % (e.event, e.src, e.dst))
    action, intent = e.event.split('_')
    if e.src == 'S0':
        if e.event == 'alert_C':
            print("End state C reached!")
        return

    if action == 'alert':
        # esrc = 'XY'
        newdst = list(e.src)
        newdst.append(intent)
        newdst = sorted(newdst)
        newdst = "".join(newdst)
        es = [es for es in endstates if es in newdst]
        if es:
            print("End state %s reached!\n" % es)
            # exit(0)

fsm = Fysom({'initial': 'S0', 'events': events, })

fsm.onchangestate = printstatechange

#fsm.alert_A(msg="fsm.current is %s\n" % fsm.current)
#fsm.clear_A(msg="fsm.current is %s\n" % fsm.current)
#fsm.alert_B(msg="fsm.current is %s\n" % fsm.current)
#fsm.alert_C(msg="fsm.current is %s\n" % fsm.current)
#fsm.alert_A(msg="fsm.current is %s\n" % fsm.current)

while True:
    t = random.choice(trans)
    a = random.choice(actions)
    if t == 'A':
        if a == 'alert':
            fsm.alert_A()
        else:
            fsm.clear_A()
    if t == 'B':
        if a == 'alert':
            fsm.alert_B()
        else:
            fsm.clear_B()
    if t == 'C':
        if a == 'alert':
            print("Alert C called.");
            fsm.alert_C()
        # clear_C is ignored.
    if t == 'L':
        if a == 'alert':
            fsm.alert_L()
        else:
            fsm.clear_L()
    if t == 'M':
        if a == 'alert':
            fsm.alert_M()
        else:
            fsm.clear_M()
    if t == 'N':
        if a == 'alert':
            fsm.alert_N()
        else:
            fsm.clear_N()
    if t == 'O':
        if a == 'alert':
            fsm.alert_O()
        else:
            fsm.clear_O()
    if t == 'P':
        if a == 'alert':
            fsm.alert_P()
        else:
            fsm.clear_P()
    if t == 'X':
        if a == 'alert':
            fsm.alert_X()
        else:
            fsm.clear_X()
    if t == 'Y':
        if a == 'alert':
            fsm.alert_Y()
        else:
            fsm.clear_Y()
    if t == 'Z':
        if a == 'alert':
            fsm.alert_Z()
        else:
            fsm.clear_Z()
    # time.sleep(1)
    

