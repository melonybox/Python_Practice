def zip_it(women, men):
	if len(women) != len(men):
		return "sizes don't match"
	return list(zip(women, men))

# ---

def is_potential_friend(set1, set2):
	if len(set1) == 1 and len(set2) == 1 and len(set1.intersection(set2)) == 1:
		return True
	return True if len(set1.intersection(set2)) >= 2 else False

#return set1 == set2 or len(set1 & set2) >= 2
# ---

def is_odd(num):
  return num % 2 != 0

# ---

def minimum_removals(lst):
	return 0 if sum(lst) % 2 == 0 else 1

# ---

def new_word(word):
	return word[-len(word)+1:]

#return word[1:]
# ---

def add_nums(nums):
	numArrPre = nums.split(", ")
	numArrPost = list(map(lambda x: int(x), numArrPre))
	return sum(numArrPost)

#return sum(map(int,nums.split(',')))
# ---
