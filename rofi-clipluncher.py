#!/usr/bin/env python3

import sys

import cliplunch

with open("clip.lunch", "r") as conf_file:
    config = cliplunch.parse_config(conf_file)

selections = {}
for item in config:
    selections[item.name] = item
    if len(sys.argv) == 1:
        print(item.name)

if len(sys.argv) == 2:
    selections.get(sys.argv[1]).launch()

