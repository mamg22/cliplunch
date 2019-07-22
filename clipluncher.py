#!/usr/bin/env python3

from typing import List

import cliplunch

conf_file = open("clip.lunch", "r")
assoc = cliplunch.parse_config(conf_file)

for i in range(len(assoc)):
    assoc[i].data["index"] = i + 1
    print(f"{assoc[i].data['index']}. {assoc[i].name}")

selection = int(input("Enter your choice: "))

def find_by_index(index:int, item_list:List[cliplunch.Launch_item]) -> cliplunch.Launch_item:
    for elem in item_list:
        if elem.data["index"] == index:
            return elem

stderr = open("/tmp/cliplunch.err", "w+") 
cliplunch.launch(find_by_index(selection, assoc), stderr)
