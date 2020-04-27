def has_key(dictionary, key):
	if key in dictionary.keys():
		return True
	else:
		return False

#return key in dictionary.keys()
# ---

def measure_the_depth(lst):
	return str(lst).count("[")

# ---

def sort_nums_ascending(lst):
	return sorted(lst)

#sort mutates and does not return, sorted does not mutate but returns
# ---

def match(s1, s2):
	return s1.casefold() == s2.casefold()

# ---

def find_index(lst, txt):
	return lst.index(txt)

# ---

def count_true(lst):
	return lst.count(True)

#count works on str and iterable
# ---

def length(s):
	if s == "":
		return 0
	else:
		return s.rindex(s[-1])+1

#The rindex() method returns the highest index of the substring inside the string (if found).
#If the substring is not found, it raises an exception.
# ---

def count_syllables(txt):
	lowerTxt = txt.lower()
	vowelCount = {}

	for vowel in "aeiou":
			count = lowerTxt.count(vowel)
			vowelCount[vowel] = count

	counts = vowelCount.values()

	return sum(counts)

#convert string to lowercase
#iterate through vowel string
#count times character is in lowercase string
#object contains character as key and count as value
#array of the object values
#sum of the array values to get the count
#return sum(1 for i in txt.lower() if i in 'aeiou')
#1 is the value to increase the sum count each time a vowel is found
# ---
