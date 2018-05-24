# mug_ical
Michigan!/usr/group iCal to email for the announce mailing list

This is a script to take the events from a CiviCRM ical feed and (at the appropriate number of days out) send that event to a mailing list.

The crontab entry for this script looks like the following:

```crontab
0 7 * *  * /home/craig/bin/mug_ical
```

And the calling script looks like:

```sh
#!/bin/sh
cd /home/craig/projects/mug_ical
/home/craig/.virtualenvs/mug_ical/bin/python mug_ical.py
```
