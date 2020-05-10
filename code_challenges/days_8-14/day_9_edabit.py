def search(lst, item):
	try:
		return lst.index(item)
	except:
		return -1

#return -1 if item not in lst else lst.index(item)
# ---

def reverse_and_not(i):
	reversedText = "".join(list(reversed(str(i))))
	return int(reversedText + str(i))

#return int(str(i)[::-1] + str(i))
# ---

def negate(lst):
	reversedArr = [-x for x in lst]
	return reversedArr

# ---

def is_it_true(relation):
	relationFixed = relation.replace("=", "==")
	return eval(relationFixed)

#return eval(relation.replace("=","=="))
# ---

def googlify(n):
	return "invalid" if n <= 1 else "G"+("o"*n)+"gle"

# ---
