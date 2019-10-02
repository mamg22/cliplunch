#!/usr/bin/env python3

import sys
import subprocess
from os.path import expanduser

import cliplunch

with open(expanduser("~/.config/cliplunch/clip.lunch"), "r") as conf_file:
    config = cliplunch.parse_config(conf_file)

selections = {}
for item in config:
    selections[item.name] = item

dmenu_input=""
for key in selections.keys():
    dmenu_input += key + "\n"

choice = subprocess.check_output("dmenu", input=bytes(dmenu_input, "utf-8")).decode("utf-8").strip()

print(choice)
selections.get(choice).launch()

