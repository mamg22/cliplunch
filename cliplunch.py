#!/usr/bin/env python3

import subprocess
import shlex

import pyperclip

class LaunchItem:
    def __init__(self, name, command):
        self.name = name
        self.command = command

    def launch(launch_item, stderr=subprocess.DEVNULL):
        subprocess.Popen(launch_item.command + ' ' + shlex.quote(pyperclip.paste().strip()), 
                         stdin=subprocess.DEVNULL, 
                         stdout=subprocess.DEVNULL, 
                         stderr=stderr, 
                         shell=True)

def parse_config(conf):
    associations = []
    for line in conf:
        if line.startswith("#"):
            continue
        sections = [ section.strip()
                     for section in line.split("|", 1) 
                     if section != ""]
        associations.append(LaunchItem(sections[0], sections[1]))
    return associations


