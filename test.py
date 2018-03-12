from datetime import datetime

date = "3/27/2018"
dateObj = datetime.strptime(date, '%m/%d/%Y')
print(dateObj.strftime("%B %d, %Y"))
