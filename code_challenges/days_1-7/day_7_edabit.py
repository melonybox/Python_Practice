def cars_needed(n):
	return n//5 if n%5 == 0 else (n//5)+1

# ---

def n_sided_shape(n):
	shapeObj = {
	1	: "circle",
	2	: "semi-circle",
	3	: "triangle",
	4	: "square",
	5	: "pentagon",
	6	: "hexagon",
	7	: "heptagon",
	8	: "octagon",
	9	: "nonagon",
	10 :	"decagon"
	}

	return shapeObj[n]

# ---

def is_truthy(val):
	return bool(val)

#return int(bool(val))
# ---

def limit_number(num, range_low, range_high):
	if num > range_low and range_high > num:
		return num
	elif range_low > num:
		return range_low
	else:
		return range_high

#a=[n,l,h]
#a.sort()
#return a[1]
#return high if n > high else low if n < low else n
# ---

def yeahNope(b):
	return "yeah" if b == True else "nope"

# ---

def add_up_to(n):
	numArr = []
	i = 0

	while n > i:
		numArr.append(i+1)
		i += 1

	return sum(numArr)

#return sum(range(1, n + 1))
#return n*(n+1)/2
# ---

def get_case(txt):
	return "lower" if txt.islower() == True else "upper" if txt.isupper() == True else "mixed"

# ---

def next_element(lst):
	nextEle = lst[1]-lst[0]
	return lst[-1]+nextEle

#return lst[-1] + (lst[1] - lst[0])
# ---

def additive_inverse(lst):
	inverseArr = [-i for i in lst]
	return inverseArr

# ---

def pos_com(num):
	totalCombo = 2
	i = 0

	while num > i:
		if i == 0:
			i += 1
		else:
			totalCombo = totalCombo*2
			i += 1

	return totalCombo

#return 2**num
# ---

def get_sequence(low, high):
	return list(range(low,high+1))

# ---
