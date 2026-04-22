#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split(",")

    # Skip header
    if data[0] == "transaction_id":
        continue

    transaction_type = data[4]
    
    print "%s\t1" % transaction_type
