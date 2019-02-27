#!/bin/env python3
from fysom import *
import yaml
# import generate_fsm
endstates = ['C', 'AB', 'XYZ']

events = {}
with open("alerts.yaml", 'r') as stream:
    try:
        events = yaml.load(stream)
    except yaml.YAMLError as ex:
        print(ex)
        exit(1)

print(events)

def printstatechange(e):
    print ('event: %s, src: %s, dst: %s' % (e.event, e.src, e.dst))
    action, intent = e.event.split('_')
    if action == 'alert':
        potential_end_state_list = sorted([intent, e.src])
        potential_end_state = "".join(potential_end_state_list)
        if potential_end_state in endstates:
            print("End state %s reached!" % potential_end_state)
        

'''

comment these out for now.  
def onalert_A(e):
    print('fan stopped.', e.msg) 
    if e.src is 'B':
        print('Send AB alert\n');

def onalert_B(e):
    print('disk full.', e.msg) 
    if e.src is 'A':
        print('Send AB alert\n');

def onalert_C(e):
    print('power loss.', e.msg) 
    print('Send C alert\n');

def onclear_A(e):
    print('clear fan stopped.', e.msg) 

def onclear_B(e):
    print('clear disk full.', e.msg) 

fsm = Fysom({'initial': 'S0', 'events': events,
             'callbacks': {
                 'onalert_A': onalert_A,
                 'onclear_A': onclear_A,
                 'onalert_B': onalert_B,
                 'onclear_B': onclear_B,
                 'onalert_C': onalert_C,
             }
            })
'''
fsm = Fysom({'initial': 'S0', 'events': events, })

fsm.onchangestate = printstatechange

fsm.alert_A(msg="fsm.current is %s\n" % fsm.current)
fsm.clear_A(msg="fsm.current is %s\n" % fsm.current)
fsm.alert_B(msg="fsm.current is %s\n" % fsm.current)
fsm.alert_C(msg="fsm.current is %s\n" % fsm.current)
fsm.alert_A(msg="fsm.current is %s\n" % fsm.current)
