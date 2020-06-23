def free_shipping(order):
	return True if sum(order.values()) > 50 else False

#return sum(order.values())>=50
# ---

def highest_digit(num):
	return max([int(x) for x in str(num)])

#return int(max(str(n)))
# ---

def capital_letters(txt):
	return sum(1 for x in txt if x.isupper())

#adds one for to the total if character is uppercase.
# ---

def max_total(nums):
	nums.sort(reverse=True)
	return sum(nums[0:5])

#return sum(sorted(nums)[-5:])
# ---

def int_or_string(var):
	return "int" if type(var) == int else "str"

#return var.__class__.__name__
# ---

def find_the_falsehoods(lst):
	falseArr = []
	for x in lst:
		if not x:
			falseArr.append(x)
	return falseArr

#return [e for e in lst if not e]
# ---
