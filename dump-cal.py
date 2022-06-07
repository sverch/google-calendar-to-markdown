#/usr/bin/env python

from ics import Calendar
import sys

with open(sys.argv[1]) as f:
    c = Calendar(f.read())

sorted_events = []
sorted_events = sorted(c.events, key=lambda k: k.begin)

for event in sorted_events:
    print("## %s: From %s\n" % (event.begin.format("MMM DD"), event.location))
    print("%s - %s:%s\n" % (
        event.begin.to('US/Eastern').format("MMM DD (h:mmA)"),
        event.end.to('US/Eastern').format("MMM DD (h:mmA)"),
        event.name.split(":")[1]))
