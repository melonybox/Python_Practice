def first_last(lst):
	newList = [lst[0],lst[-1]]
	return newList

# ---

def min_max(nums):
	newList = [min(nums),max(nums)]
	return newList

# ---

def how_many_times(num):
	edaString = "Ed{}bit"
	return edaString.format("a"*num)

# ---

def flip_bool(b):
	if b == 0:
		return bool(1)
	else:
		return bool(0)

#how to do a bang/double bang like in js?
# ---

def string_int(txt):
	return int(txt)

# ---

def count_claps(txt):
	return txt.count("C")

# ---

def stack_boxes(n):
	return n*n

# ---
