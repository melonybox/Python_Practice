def first_last(lst):
	newList = [lst[0],lst[-1]]
	return newList

# ---

def min_max(nums):
	newList = [min(nums),max(nums)]
	return newList

# ---

def how_many_times(num):
	edaString = "Ed{}bit"
	return edaString.format("a"*num)

# ---

def flip_bool(b):
	if b == 0:
		return bool(1)
	else:
		return bool(0)

#return not b
#how to do a bang/double bang like in js?
# ---

def string_int(txt):
	return int(txt)

# ---

def count_claps(txt):
	return txt.count("C")

# ---

def stack_boxes(n):
	return n*n

# ---

def get_fillings(sandwich):
	return sandwich[1:len(sandwich)-1]

# ---

def flip(y):
	if not y == 1:
		return 1
	else:
		return 0

# ---

def long_burp(num):
	formatR = "r"*num
	resultR = "Bu"+formatR+"p"
	return resultR

# ---

def is_empty(dictionary):
	if len(dictionary) == 0:
		return True
	else:
		return False

# ---

def less_than_100(a, b):
	if a+b < 100:
		return True
	else:
		return False

# ---

def divides_evenly(a, b):
	if a%b == 0:
		return True
	else:
		return False

# ---

def potatoes(potato):
	return potato.count("potato")

# ---

def check_equals(lst1, lst2):
	if lst1 == lst2:
		return True
	else:
		return False

# ---

def equal_slices(total, people, each):
	sliceTotal = people*each
	if people == 0:
		return True
	else:
		if sliceTotal <= total:
			return True
		else:
			return False

# ---

def check_equality(a, b):
	if a is b:
		return True
	else:
		return False

# == compares the values of the objects.
# is compares the references of the objects.
# ---

import re

pattern = '\w+'

#shorthand regex
# ---

def has_bugs(buggy_code):
	if buggy_code:
		return 'sad days'
	else:
		return 'it\'s a good day'

# ---

def has_same_bread(lst1, lst2):
	sandA = [lst1[0],lst1[-1]]
	sandB = [lst2[0],lst2[-1]]
	return sandA == sandB

#return lst1[0] == lst2[0] and lst1[-1] == lst2[-1]
# ---

def char_count(txt1, txt2):
	return txt2.count(txt1)

# ---

def equation(s):
	return eval(s)

# 1+1 or 1+1+1 or 2*3+1
# ---

def same_case(txt):
	return txt.islower() or txt.isupper()

# ---

def get_word(left, right):
	newWord = left+right
	return newWord.capitalize()

#return (left+right).capitalize()
# ---
