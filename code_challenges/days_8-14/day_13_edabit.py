template = "My {0} is {me}. His {0} is {him}."

# ---

def count_words(txt):
	return len(txt.split(" "))

# ---

def add_ending(lst, ending):
	return ["{}{}".format(i,ending) for i in lst]

# ---

def int_within_bounds(n, lower, upper):
	if type(n) is float:
		return False
	return n >= lower and upper > n

#return n in range(lower, upper)
# ---

def ink_levels(inks):
	return min(inks.values())

# ---

def is_in_range(n, r):
	return n >= r["min"] and r["max"] >= n

#return r['min'] <= n <= r['max']
# ---

def increment_items(lst):
	return [i+1 for i in lst]

# ---

def equilibrium(x):
	return "positive" if x > 0 else "negative" if x < 0 else True

# ---

def first_one(a, b=None, c=None, d=None):
	return a or b or c or d or "not found"

#return first truthy, else return "not found"
# ---

def detect_word(txt):
	smallText = []
	for i in txt:
		if i.islower() == True:
			smallText.append(i)
	return "".join(smallText)

#return "".join(c for c in txt if c.islower())
# ---
