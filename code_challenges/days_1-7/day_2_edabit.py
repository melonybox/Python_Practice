def halfQuarterEighth(n):
	return [n/2,n/4,n/8]

# ---

def divide(a,b):
	try:
		return a/b
	except:
		return "Error"

# Cant divide by 0
# ---

def And(a,b):
	if a and b:
		return True
	else:
		return False

# And operator test
# ---

def squared(a):
	return a * a

# Syntax error fix
# ---

def subtraction(a,b):
	return a-b

# ---

def get_container(product):
	matches = {
	"Bread" : "bag",
	"Milk" : "bottle",
	"Beer" : "bottle",
	"Eggs" : "carton",
	"Cerials" : "box",
	"Candy" : "plastic",
	"Cheese" : None
	}
	return matches[product]

# ---

def get_sum_of_elements(lst):
	return sum(lst)

# add all numbers of array/list together
# ---

def is_last_character_n(word):
	return word.endswith("n")

# ---

def is_safe_bridge(s):
	if " " not in s:
		return True
	else:
		return False

# check if string does not contain space, "## ###" vs "#####"
# ---
