#!/usr/bin/env python3

import cliplunch

conf_file = open("clip.lunch", "r")

assoc = cliplunch.parse_config(conf_file)

options = {}
for index, name in enumerate(assoc, 1):
    options[index] = name
    print(f"{index}. {name}")

selection = int(input("Enter your choice: "))

stderr = open("/tmp/cliplunch.err", "w+") 

cliplunch.launch(assoc[options[selection]], stderr)
