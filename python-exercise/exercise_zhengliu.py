#!/usr/bin/python

def is_leap_year(year):
  """Returns if given year is leap year"""
  if year % 4 == 0: 
    if year % 100 == 0: 
      if year % 400 == 0:
        return True
      return False
    return True
  return False

def day_of_year(year, month, day):
  """Returns the day of the year for given date"""
  month_day_dict = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10:31,
    11:30,
    12:31,
  }
  if year < 0:
    print "invalid year:", year
    return
  if month <= 0 or month > 12:
    print "invalid month:", month
    return
  if day > month_day_dict[month]:
    print "invalid date:", day
    return
  result = 0
  if is_leap_year(year):
    month_day_dict[2] = 29
  for mt in xrange(1, month):
    result = result + month_day_dict[mt]
  return result + day

print day_of_year(2016,2,1)
