## Dictionaries
You can check if a dictionary is empty by just doing:
'''python
if dictName:
    print("There's something in the dictionary")    
else
    print("The dictionary is empty")
'''

You can see if there is an entry for a given key in a dictionary by just check in i.e.
'''python
if findVal in dictName:
    print("Found {0} in the dictionary".format(findVal))
else
    print("{0} not in dictionary")
'''

## Date Times
To convert a string like "01/23/2018" to a datetime, use the function strptime, which takes a string and a format string.  [Here](http://strftime.org/) is a list of useful formats.
'''python
     self.transDate = datetime.strptime(arg[0], '%m/%d/%Y')
'''
