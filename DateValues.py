# Personal library of Common Date and Time Values for use 

from datetime import date, datetime, timedelta

Today = date.today()   

def GetFirstNextMonth():
#get the first day of the following month

    FirstNextMonthStr = date(Today.year + (Today.month // 12), ((Today.month % 12) + 1), 1)
    return FirstNextMonthStr

def GetLastPrevMonth():
#get the last day of the previous month

    LastPrevMonthStr = date(Today.year, Today.month, 1) - timedelta(days=1)
    return LastPrevMonthStr

def GetLastThisMonth():
#get the last day of the current month

    LastThisMonthStr = date(Today.year + (Today.month // 12), ((Today.month % 12) + 1), 1) - timedelta(days=1)
    return LastThisMonthStr

def GetFirstNextYear():
#get the first day of the following year
 
    FirstNextYearStr = date(Today.year + 1, 1, 1)
    return FirstNextYearStr

def GetNumDaysTillEndMonth():
#get the number of days till the end of the month

    NumDaysTillEndMonth = GetLastThisMonth() - Today
    return NumDaysTillEndMonth.days

def GetNumDaysInRange(StartDate, EndDate):
#get the number of days between two dates

    NumDaysInRange = EndDate - StartDate
    return NumDaysInRange.days
