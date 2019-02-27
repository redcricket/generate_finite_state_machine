#!/bin/env python3
from itertools import combinations
"""
"""

input = ['A', 'B', 'C', 'X', 'Y', 'Z']
endstates = ['C', 'AB', 'XYZ']

states = []
trans = [ 'alert_%s' % a for a in input ]
trans.extend ([ 'clear_%s' % a for a in input ])
print (trans)
# exit(0)
output = sum([list(map(list, combinations(input, i))) for i in range(len(input) + 1)], [])
for out in output:
    state = ''.join(out)
    endstate_in_state = [es for es in endstates if es in state]
    if not endstate_in_state:
        states.append(state)
#states[0]='S0'
for s in states:
    print(s)

def dst(t,s):
    action, intent = t.split('_')
    if action == 'alert':
        if s == intent:
            return(s)
        s = '%s%s' % (s,intent)
        # remove dups
        set_s = set(list(s))
        s = list(set_s)
        s = "".join(sorted(s))
        # print(s)
        endstate = [es for es in endstates if es in s]
        if endstate:
            s = s.replace(endstate[0],'') 
    else:
        s = s.replace(intent,'')
        print ("Action is %s new s is %s" % (action, s))

    if s is '':
        s = 'S0'
    return(s)

yaml = "---\n"
for t in trans:
    for s in states:
        d = dst(t,s)
        if d == s:
            continue
        if s is '':
            s = 'S0'
        yaml += ''' - name: '%s'
   src: '%s'
   dst: '%s'
''' % ( t, s, d )
print(yaml)
