#!/usr/bin/env python3

from typing import List

import cliplunch

with open("clip.lunch", "r") as conf_file:
    config = cliplunch.parse_config(conf_file)

selections = {}
for index, launch_item in enumerate(config, 1):
    selections[str(index)] = launch_item
    print(f"{index}. {launch_item.name}")

selection = input("Enter your choice: ")
item = selections.get(selection)
if item is None:
    print("Invalid Option")
else:
    with open("/tmp/cliplunch.err", "w+") as stderr:
        item.launch(stderr)
