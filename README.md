# README
Black Stars Rise is a tabletop roleplaying game. This repo contains the entire text of the game, plus a simple AppEngine app to display it, and the InDesign files mapped to the text.

## Guide
Here's your quick tour to what's here:

### app.yaml
AppEngine configuration.

### build.py
Really horrible python script to take the raw XML and present it for InDesign layout.

### configuration/
Contains files that describe in python the structure of the book. If you're looking to add or rearrange entire parts of the book, configuration/setup.py is your place.

### css/
Styles for the web app. Not shared with InDesign in any way. Wouldn't it be nice if they were?

### favicon.ico
Site icon.

### fonts/
Bootstrap glyphicons. Not really used, but since they're part of the regular Bootstrap distro keeping them anyway. All actual web fonts come from Google Fonts.

### js/
Bootstrap javascript. Probably don't touch it.

### LICENSE
Everything's CC-BY!

### main.py
AppEngine entry point. Pretty much boilerplate. Only one handler, which renders a book part.

### templates/
Jinja templates for web presentation. If you want to change the HTML of the web version, look here.

### text/
The raw XML which gets parsed out for both web and print. Broken down into logical units which are assembled by setup.py into a book.

### THANKS.md
Contributors. If you submit a pull request feel free to add yourself here as well.