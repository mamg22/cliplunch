#!/usr/bin/env python3

import subprocess
import shlex
from typing import IO, List

import pyperclip

class Launch_item:
    def __init__(self, name: str, command: str, data:dict={}):
        self.name = name
        self.command = command
        self.data = data

    def set_data(self, key:str, value) -> None:
        self.data[key] = value

def parse_config(conf: IO[str]) -> List[Launch_item]:
    associations = []
    for line in conf:
        try:
            sections = list(map(lambda section: section.strip(), line.split("|", 1)))
            associations.append(Launch_item(sections[0], sections[1]))
        except ValueError as ex:
            pass
    return associations

def launch(launch_item: Launch_item, stderr: IO[str]=subprocess.DEVNULL) -> None:
    subprocess.Popen(launch_item.command + ' ' + shlex.quote(pyperclip.paste().strip()), 
                     stdin=subprocess.DEVNULL, 
                     stdout=subprocess.DEVNULL, 
                     stderr=stderr, 
                     shell=True)

