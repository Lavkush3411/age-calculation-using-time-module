i=input("enter your `birthdate seprating by '-' = ")
a=i.split("-")
d=map(int,a)
import datetime
b=datetime.datetime(*d)
c=datetime.datetime.now()
year=(c-b)//datetime.timedelta(days=365.25)
e=(c-b)%datetime.timedelta(days=365.25)
print(year,"year",e)
i=input("enter your `birthdate seprating by '-' = ")
a=i.split("-")
d=map(int,a)
import datetime
b=datetime.datetime(*d)
c=datetime.datetime.now()
year=(c-b)//datetime.timedelta(days=365.25)
e=(c-b)%datetime.timedelta(days=365.25)
print(year,"year",e)