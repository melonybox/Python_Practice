def is_equal(num1, num2):
	if type(num1) and type(num2) == int:
		return num1 == num2
	return False

#return isinstance(num1, int) and isinstance(num2, int) and num1 == num2
# ---

def match_houses(step):
	if step <= 0:
		return 0
	return (step*6) - (step-1)

# ---

import math

def mystery_func(lst, n):
  return [math.floor(x%n) for x in lst]

#return [i%n for i in lst]
# ---

def reverse(txt):
	strArr = list(txt)
	strArr.reverse()
	return "".join(strArr)

#return s[::-1]
# ---

def city_facts(city):
	strFormat = "{} has a population of {} and is situated in {}"
	return strFormat.format(city['name'],city['population'],city['continent'])

#return "{} has a population of {} and is situated in {}".format(city['name'], city['population'], city['continent'])
# ---

def reverse_list(num):
	numArr = [int(x) for x in str(num)]
	numArr.reverse()
	return numArr

#return [int(i) for i in str(num)[::-1]]
#string[::-1] reverse a string
# ---

def is_identical(s):
	return True if len(set(s)) == 1 else False

#return len(set(s)) == 1
# ---

def same(a1, a2):
	return len(set(a1)) == len(set(a2))

# ---
