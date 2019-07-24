# Cliplunch

Cliplunch is a library and a series of programs that call a program with your clipboard's content as argument.

Clipluncher is a simple implementation of a command line luncher.

rofi-clipluncher is a luncher designed to be used as a rofi modi.

## Config files

Cliplunch configuration files (just for now, may change later) follow the format:

    <name>|<command>

One name/command pair per line. name is the alias for the command and command is the command, where the clipboard is pasted at the end (for now).

Lines starting with `#` are considered comments and are ignored.

Cliplunch configuration files have the extension `.lunch`, the default configuration file is `clip.lunch`.

Leading and trailing whitespace is striped from the name, command and the pasted text.

## TODO and (possible) future features

* Allow the clipboard paste be placed anywhere in the command, not just at the end
* Decide on a config file format.
* Allow running a fallback program on failure (e.g. notification when mpv can play given video)
* Allow the user to specify a different lunchfile.

## Why that name?

[Started thinking a name, felt hungry, "cliplunch" it is.](https://www.youtube.com/watch?v=B0RPDXt6m1s)
