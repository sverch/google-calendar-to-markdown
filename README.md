# Google Calendar to Markdown

Simple instructions and script to get a markdown file from a google calendar.

1. [Export Your Calendar](https://support.google.com/calendar/answer/37111?hl=en)
2. Unzip the zipfile.
3. Install [poetry](https://python-poetry.org/).
4. Install dependencies with `poetry install`.
5. Run script to dump markdown from the file you unzipped `poetry run python
   dump-cal.py <calendar>\@group.calendar.google.com.ics`
