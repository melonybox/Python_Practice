def calc_determinant(matrix):
	return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

#(a, b), (c, d) = matrix
#return a * d - b * c
# ---

def sum_even_nums_in_range(start, stop):
	numRange = list(range(start,stop+1))
	evenNumRange = list(filter(lambda x: x%2 == 0, numRange))
	return sum(evenNumRange)

#return sum(i for i in range(start, stop+1) if not i%2)
# ---

def sum_of_cubes(nums):
	return sum(i**3 for i in nums)

# ---

def yen_to_usd(yen):
	return round(yen/107.5, 2)

# ---

def test_jackpot(result):
	return True if len(set(result)) == 1 else False

# ---

def count_unique(s1, s2):
	combinedStr = s1 + s2
	return len(set(list(combinedStr)))

#list(str) seperates per character
# ---

def skip_the_sugar(drinks):
	sugarDrink = ["cola","fanta"]
	return list(filter(lambda x: x not in sugarDrink, drinks))

# ---

def say_hello_bye(name, num):
	return "Hello " + name.capitalize() if num == 1 else "Bye " + name.capitalize()

# ---
