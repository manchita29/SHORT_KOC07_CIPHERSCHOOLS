a= input("enter date 1")
b= input("enter date 2")
print(a,b)
year1 = int(a.split('/')[-1])
year2 = int(b.split('/')[-1])
leap_years=["leap years : " ]
non_leap_years=["non leap years:" ]
for year in range(year1,year2):
  if (year%4==0 and year%100!=0) or (year%400==0):
    leap_years.append(year)
  else:
    non_leap_years.append(year)
print(leap_years)
print(non_leap_years)
0 comments on commit 7a58b88
