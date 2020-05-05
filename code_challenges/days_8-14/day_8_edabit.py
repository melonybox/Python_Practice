def calculate_scores(txt):
	return [txt.count("A"),txt.count("B"),txt.count("C")]

#return [txt.count(x) for x in 'ABC']
# ---

def score_calculator(easy, med, hard):
	numArr = [easy,med,hard]
	for number in numArr:
		if number < 0:
			return "invalid"
	return easy*5 + med*10 + hard*20

#return 5*e+10*m+20*h if e+m+h == abs(e)+abs(m)+abs(h) else 'invalid'
# ---

def is_triangle(a, b, c):
	return True if a+b > c and a+c > b and b+c > a else False

# ---

def greater_than_one(frac):
	return True if eval(frac) > 1 else False

# ---

def both(n1, n2):
	return True if n1 > 0 and n2 > 0 or n1 == 0 and n2 == 0 or n1 < 0 and n2 < 0 else False

# ---

def pH_name(pH):
	if pH > 14 or pH < 0:
		return "invalid"
	return "alkaline" if pH > 7 else "acidic" if pH < 7 else "neutral"

# ---

def convert(data1, data2):
	if type(data1) == list:
		return list(data2)
	elif type(data1) == tuple:
		return tuple(data2)
	else:
		return set(data2)

#return type(data1)(data2), list(data2), tuple(data2), set(data2)
#in sets {} order does not matter for comparisons
# ---

def add_odd_to_n(n):
	oddSum = 0
	for i in range(1,n+1):
		if i%2 != 0:
			oddSum += i

	return oddSum

#return ((n+1)//2)**2
#range(1, n+1, 2), 2 increments it here
# ---
