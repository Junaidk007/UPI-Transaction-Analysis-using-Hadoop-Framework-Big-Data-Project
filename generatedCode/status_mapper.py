#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split(",")

    if data[0] == "transaction_id":
        continue

    status = data[3]
    print "%s\t1" % status
