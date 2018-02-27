# Some Settings.py notes

The timezone is set.  You can see a [list of timezone names](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) on Wikipedia.  I set it to 'America/Chicago'.  If you don't do this, the times that show up in the admin console are for the default TIME_ZONE, 'GMT'.

Installed Apps is the list of apps that make up the site.  By default there are things for the admin console, auth stuff, sessions, messages and static files.  To create the polls app I added:
'polls.apps.PollsConfig'.  PollsConfig is in apps.py file in the APP directory that was created when I did the
>startapp polls
to spit out the application.