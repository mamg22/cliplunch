#!/usr/bin/env python3

import subprocess
import shlex
import typing

import pyperclip

class launch_item:
    # not used still, need to decide a config format
    def __init__(self, name, command, index, options={}):
        self.name = name
        self.command = command
        self.index = index
        self.options = options

def parse_config(conf: typing.IO[str]) -> dict:
    associations = {}
    for line in conf:
        try:
            name, command = map(lambda section: section.strip(), line.split("|", 1))
            associations[name] = command
        except ValueError as ex:
            pass
    return associations

def launch(command: str) -> None:
    subprocess.Popen(command + ' ' + shlex.quote(pyperclip.paste().strip()), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

