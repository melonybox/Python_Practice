def get_multiplied_list(lst):
	multLst = map(lambda x: x*2, lst)
	return list(multLst)

#Map in python very different then javascript / ruby.
#lambda = anon function
# ---

def total_cups(n):
	return (n//6)+n

#Floor operator while divide
# ---

def sum_first_n_nums(lst, n):
	return sum(lst[0:n])

# ---

def number_syllables(word):
	return word.count("-")+1

# ---

def missing_angle(angle1, angle2):
	missAngle = 180-(angle1+angle2)
	if missAngle > 90 and 180 > missAngle:
		return "obtuse"
	elif missAngle == 90:
		return "right"
	else:
		return "acute"

# ---

def word_lengths(lst):
	lenLst = map(lambda x: len(x), lst)
	return list(lenLst)

# ---

def can_nest(list1, list2):
	return not any(x in list1 for x in list2)

#not makes false -> true and true -> false
#not == !! in javascript
# ---

def should_serve_drinks(age, on_break):
	return True if age >= 18 and on_break == False else False

#return age >= 18 and not on_break, was trying to do this at first
# ---

def wumbo(words):
	return words.replace("M", "W")

#return ''.join([i if i != 'M' else 'W' for i in words]), another way
# ---
