# Cliplunch

Cliplunch is a library and a series of programs that call a program with your clipboard's content as argument.

Clipluncher is a simple implementation of a command line luncher.

rofi-clipluncher is a luncher designed to be used as a rofi modi.

## Config files

Cliplunch configuration files (just for now, may change later) follow the format:

    <name>|<command>

One name/command pair per line. name is the alias for the command and command is the command, where the clipboard is pasted at the end (for now).

Cliplunch configuration files have the extension `.lunch`, the default configuration file is `clip.lunch`.

Leading and trailing whitespace is striped from the name, command and the pasted text.

## TODO

* Allow the clipboard paste be placed anywhere in the command, not just at the end
* Decide on a config file format.
* Allow running a fallback program on failure (e.g. notification when mpv can play given video)

## Why that name?

Felt hungry thinking a name, "cliplunch" came to my mind, Bon Appétit.
