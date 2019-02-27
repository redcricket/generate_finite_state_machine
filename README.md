# generate_finite_state_machine
Python script that will generate a finite state machine.

This project is still at a very primitive state.

There are issue like hardcoding key variables like:

```
input = ['A', 'B', 'C', 'X', 'Y', 'Z']
endstates = ['C', 'AB', 'XYZ']
```

The point of these variables is to define the states and transitions.
The values of `input` causes generate_fsm.py to generate these transitions:

alert_A, alert_B, alert_C, alert_X, alert_Y, alert_Z, clear_A, clear_B, clear_C, clear_X, clear_Y and clear_Z.

And these states: A, B, X, Y, Z, AX, AY, AZ, BX, BY, BZ, XY, XZ, YZ, AXY, AXZ, AYZ, BXY, BXZ, and BYZ.

An `alert` transition could be something like a disk filling up or a network interface going down. The `clear` tranistion
would be the oppisite of the alert. Like the disk space improving or the network interface going up.

endstate means that a special/goal state where some action is to take place like sending an email or paging a sys admin.

## How It Works.

Run the `genrate_fsm.py` script like so:

```
./generate_fsm.py > alerts.yaml
```

(!) Make the edit described in the Known Issues section below.

Now run `alerts.py` like so: 

```
$ ./alerts.py
event: alert_A, src: S0, dst: A
event: clear_A, src: A, dst: S0
event: alert_B, src: S0, dst: B
event: alert_A, src: B, dst: S0
End state AB reached!
```

## Known Issue

Currently the single state endstates are not handling by the generate_fsm.py script, but the work around is easy.

For example I just add these lines to geneated yaml file:

```
 - name: 'alert_C'
   src: '*'
   dst: '='
```

### More known issues

many corner cases to be dealt with here and example diff of alerts.ayml to illistrat the point:

```
+ - name: 'alert_A'
+   src:
+     - 'A'
+     - 'AX'
+     - 'AY'
+     - 'AZ'
+     - 'AXY'
+     - 'AXZ'
+     - 'AYZ' 
+   dst: 'A'
  - name: 'alert_A'
    src: 'BYZ'
    dst: 'YZ'
@@ -122,6 +132,14 @@
  - name: 'alert_X'
    src: 'BYZ'
    dst: 'B'
+ - name: 'alert_X'
+   src: 
+     - 'AX'
+     - 'BX'
+     - 'X'
+     - 'XY'
+     - 'XZ'
+   dst: 'X' 
  - name: 'alert_Y'
    src: 'S0'
    dst: 'Y'
@@ -242,6 +260,19 @@
  - name: 'clear_B'
    src: 'BYZ'
    dst: 'YZ'
+ - name: 'clear_B'
+   src:
+     - 'A'
+     - 'AX'
+     - 'AY'
+     - 'AZ'
+     - 'X'
+     - 'Y'
+     - 'Z'
```

and here the bugs it causes.


```
$ ./random_test.py 
...
event: alert_X, src: S0, dst: X
event: alert_Z, src: X, dst: XZ
event: clear_X, src: XZ, dst: Z
Traceback (most recent call last):
  File "./random_test.py", line 70, in <module>
    fsm.alert_Z()
  File "/home/plankton/STATEMACHINE/env/lib/python3.6/site-packages/fysom/__init__.py", line 272, in fn
    "event %s inappropriate in current state %s" % (event, self.current))
fysom.FysomError: event alert_Z inappropriate in current state Z
(env) 
```
