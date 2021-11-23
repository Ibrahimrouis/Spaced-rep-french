import random
import numpy
from datetime import date, timedelta
import pickle

order=[]
for i in range(10,1021):
    while True:
        new=random.randint(10,1021)  
        if new not in order:
            break
    order.append(new)

days={1:[1],2:[1],3:[1,2],4:[2],5:[2,3],6:[3,4],7:[4,5],8:[7,8,9],9:[15,16,17],10:[28,29,30,31]}
today=date.today()

logs={}
## two pages first two days then one page by day
logs.update({order[0]:{0:today},order[1]:{0:today}})
logs.update({order[2]:{0:today+timedelta(1)},order[3]:{0:today+timedelta(1)}})
day=today
for key in days:
    day=day+timedelta(random.choice(days[key]))
    logs[order[0]].update({key:day})
day=today
for key in days:
    day=day+timedelta(random.choice(days[key]))
    logs[order[1]].update({key:day})
day=today+timedelta(1)
for key in days:
    day=day+timedelta(random.choice(days[key]))
    logs[order[2]].update({key:day})
day=today+timedelta(1)
for key in days:
    day=day+timedelta(random.choice(days[key]))
    logs[order[3]].update({key:day})

## we generate other dates and we avoid wednesdays and weekends
firstday=today+timedelta(2)
for i in range(4,len(order)):
    firstday=firstday+timedelta(1)
    if firstday.weekday()==2:
        firstday=firstday+timedelta(1)
    if firstday.weekday()==(5 or 6):
        firstday=firstday+timedelta(7-firstday.weekday())
    logs.update({order[i]:{0:firstday}})
    day=firstday
    for key in days:
        day=day+timedelta(random.choice(days[key]))
        logs[order[i]].update({key:day})


pickle.dump( logs, open( "planning.pkl", "wb" ) )
