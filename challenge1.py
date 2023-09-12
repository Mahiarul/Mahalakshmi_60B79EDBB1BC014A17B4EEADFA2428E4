def fact_rec(n):
  if n == 0 or n == 1:
    return 1  # Fix the base cases: return 1 instead of 0 for factorial
  else:
    return n * fact_rec(n - 1)


number = 2
res = fact_rec(number)
print("the factorial of {} is {}".format(number, res))


def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False


year = int(input("Enter a year: "))

if is_leap_year(year):
  print(year, "is a leap year.")
else:
  print(year, "is not a leap year.")
