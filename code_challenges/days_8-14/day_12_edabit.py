def squares_sum(n):
	newArr = [i**2 for i in range(1, n+1)]
	return sum(newArr)

#return sum(i*i for i in range(1, n+1))
# ---

def roger_shots(lst):
	singleBang = lst.count("Bang!")
	doubleBang = lst.count("BangBang!")
	return singleBang*0.5 + doubleBang*0.5

#return sum(i in ('Bang!', 'BangBang!') for i in lst)/2
# ---

def space_me_out(s):
	strArr = list(s)
	spaceChar = " "
	return spaceChar.join(strArr)

#return ' '.join(s)
#this is a thing you can do it seems.
#dont even have to split first like in js.
# ---

def is_leap(year):
	if year%4 == 0 and year%100 != 0:
		return True
	elif year%400 == 0:
		return True
	else:
		return False

#return year%400 == 0 or (year%4 == 0 and year%100 != 0)
# ---

template = "Their names were: {}, {} and {}."

# ---

def get_vote_count(votes):
	return votes["upvotes"] - votes["downvotes"]

#votes.get("upvotes", default_value)
#would return default_value if no key, or None if no default is provided
# ---
