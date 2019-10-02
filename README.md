# Cliplunch

Cliplunch is a library and a series of programs that call a program with your clipboard's content as argument.

Clipluncher is a simple implementation of a command line luncher.

rofi-clipluncher is a luncher designed to be used as a rofi modi.

dmenu-clipluncher uses dmenu to provide lunching options.

## Config files

Cliplunch configuration files (just for now, may change later) follow the format:

    <name>|<command>

One name/command pair per line. name is the alias for the command and command is the command, where the clipboard is pasted at the end (for now).

Lines starting with `#` are considered comments and are ignored.

Cliplunch configuration files have the extension `.lunch`, the default configuration file is `clip.lunch`.

Leading and trailing whitespace is striped from the name, command and the pasted text.

## TODO and (possible) future features

* Allow the clipboard paste be placed anywhere in the command, not just at the end
* Allow the user to specify a different lunchfile.

## Why?

Many things you can do:

* Copy a video URL, and download it to your video directory using `youtube-dl` after picking a video resolution.
* Don't like a web video player? Play it in `mpv`, `mplayer` or whatever you like.
* Need to see an image, but want it outside your browser? Open it in `feh`.
* Want to download that image to `~/memes-to-repost-in-a-week/`? Do it easily.
* Found some interesting quote you want to keep? Append it to your `wonderful-quotes-i-found-in-the-internet.txt` file.
