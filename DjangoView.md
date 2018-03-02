# Django tutorial part 3 Views

Django uses the URL Dispacther and 'URLconfs' to map URL patterns to views.  A pattern is the general form of the URL i.e. /newsarchive/<year>/<month>/

Inside path function call in urls.py, things in angle brackets (<>) "capture" a variable so it can be used in the view call i.e.

```python
path('<int:question_id>/', view.detail, name='detail')
```

if an integer pattern is found like 34/, view.detail(request, question_id=34) will be called.

So you could create a view that builds the page and returns the http response, but that would be hard coding the design of the page in with the view and it would be better to separate the two.  We can use Django's templating system to do this.

Djangos's TEMPLATES setting specifies some of the details about templating i.e. what templating system (by defualt its Django's), if **APP_DIRS** are used, and more.

The templates are put an additional level down in the app directory under the AppName so it is "namespaced" i.e. if there were 2 index.html in 2 different apps, Django can tell the difference.

You can use the Django.shortcuts method render(request, 'polls/index/html', context) to render the specific context.  A context is a dictionary of stuff to send to be used in the template.

```python
from django.shortcuts import get_object_or_404, render

from ./models import Question
#...
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/details.html', {'question: question'})
```

Lastly, the templating system uses dot-lookup syntax to access variable attributes i.e. **{ question.question_text }**.  First Django does a dictionary lookup on the object **question**, failing that it tries an attribute lookup - 

