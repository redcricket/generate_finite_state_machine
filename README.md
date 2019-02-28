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

Now run `alerts.py` like so: 

```
$ ./random_test.py 
event: alert_A, src: S0, dst: A
event: clear_A, src: A, dst: S0
...
event: alert_B, src: S0, dst: B
event: alert_A, src: B, dst: S0
End state AB reached!
...
^C
```
