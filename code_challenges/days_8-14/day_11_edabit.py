def football_points(wins, draws, losses):
	return wins*3 + draws

# ---

def minus_one(lst):
	arr = lst.copy()
	arr.pop()
	return arr

#does not mutate the original list
# ---

def get_triangle_type(lst):
	if len(lst) != 3:
		return "not a triangle"

	triArr = set(lst)

	if len(triArr) == 1:
		return "equilateral"
	elif len(triArr) == 2:
		return "isosceles"
	else:
		return "scalene"

#if len(lst) == 3:
#		return ['equilateral', 'isosceles', 'scalene'][len(set(lst)) - 1]
#	return 'not a triangle'
# ---

def variable_valid(var):
	return True if var.isidentifier() == True else False

# ---

def mean(nums):
	return round(sum(nums)/len(nums), 1)

# ---

import math

def vol_pizza(radius, height):
	return round((radius**2*height)*math.pi)

# ---

def reverse_capitalize(txt):
	return txt[::-1].upper()

# ---

template = "{1} hit {0} and then {0} hit {1}."

# ---

def modify_last(txt, n):
	strLst = list(txt)
	multiText = txt[-1]*n
	strLst[-1] = multiText
	return "".join(strLst)

#return txt+txt[-1]*(n-1)
# ---
