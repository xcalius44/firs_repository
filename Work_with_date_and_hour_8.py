from datetime import date

def numOfDays(): 
    y1 = int(input())
    m1 = int(input())
    d1 = int(input())
    carent_date = date.today()
    date1 = date(y1, m1, d1)
    date2 = date(carent_date.year ,carent_date.month ,carent_date.day)
    answer = (date2-date1).days
    print(answer // 365)
numOfDays()
