# Some Settings.py notes

The timezone is set.  You can see a [list of timezone names](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) on Wikipedia.  I set it to 'America/Chicago'.  If you don't do this, the times that show up in the admin console are for the default TIME_ZONE, 'GMT'.

Installed Apps is the list of apps that make up the site.  By default there are apps for the admin console, auth stuff, sessions, messages and static files.  To create the polls app I added:
'polls.apps.PollsConfig' into the installed apps.  PollsConfig is in apps.py file in the APP directory that was created when I did the:

>startapp polls

to spit out the application.

Once an app is made, if there are database changes, you have to run:

>python manage.py migrate

and the necessary changes are made to the database that is configured as specified in the **DATABASE** setting.

Another file that **python manage.py appstart {AppName}** creates in the model directory is models.py.  You create models by subclassing **django.db.models.Model**.  Each model has a number of class variables that are the class variable for the object and each of those represents a database field.

```python
from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	# add str "introspective method"
	def __str__(self):
	    return self.question_text```

Note that type(Question) is <QuerySet>, and therefore you can use db like operations like .filter(), or .get(pk=1) to get individual results.

Each field is represented as an instance of class **Field**: **CharField** for character, **DateTimeField** for datetimes.  This is how django knows the data type.  The name becomes the name of the database field.  The field name is "machine readable", but you can add a optional parameter to designate a human readable format like 'date published' and that will be used in "introspective" parts of Django i.e. print statements and ??.

With this definition, Django can create the table, add constraints, set default values, AND create a python DB access API for the objects.

To make the polls app modifyable in the admin interface you need to add the table(s) in polls/admin.py.

>puthon manage.py makemigration {AppName} polls

creates the DB specific migration file in migration folder inside the /app directory, that migrate uses to perform the DB changes.

Migrations are saves so you can commit them to the repo and run them on a new db in a different environment i.e. qa or production.