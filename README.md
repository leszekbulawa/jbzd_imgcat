# JBZD imgcat
This small script prints random image from jbzd.pl main page to terminal.

It uses iTerm2 utilities (imgcat) to display images in console.

In future it will cover more terminal emulators and image printing programs.
Over time it will be available in PyPI.

## Prequisities

- iTerm2
- iTerm2 utilities (Shell Integration) - imgcat
- python 3
- python3 libs: `requests`, `BeautifulSoup4`

## Usage
curl -s "$(python3 get_url.py)" | imgcat
