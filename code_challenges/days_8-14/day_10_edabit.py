def is_even(n):
	return n % 2 == 0

#returns true or false
# ---

def word(s):
	numObj = {
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9,
	"zero": 0,
	}
	return numObj[s]

# ---

def operation(num1, num2):
	if num1 + num2 == 24:
		return "added"
	elif num1 - num2 == 24:
		return "subtracted"
	elif num1 * num2 == 24:
		return "multiplied"
	elif num1 / num2 == 24:
		return "divided"
	else:
		return None

#return {a+b: "added", a-b: "subtracted", a*b: "multiplied", a/b: "divided"}.get(24)
#first encounter with get on a obj
# ---

def nothing_is_nothing(*args):
	return all(args)

#all checks if all in an iterable are true or false
# ---

def search(lst, item):
	return -1 if item not in lst else lst.index(item)

# ---

def volume_of_box(sizes):
	boxVals = sizes.values()
	boxVolume = 0
	for x in boxVals:
		if boxVolume == 0:
			boxVolume = x
		else:
			boxVolume *= x
	return boxVolume

#w, l, h = sizes.values()
#return w * l * h
#similur to destructuring
# ---

def say_hello_bye(name, num):
	capsName = name.capitalize()
	helloText = "Hello " + capsName
	byeText = "Bye " + capsName
	return helloText if num == 1 else byeText

# ---

def is_palindrome(txt):
	return txt == txt[::-1]

#[::-1] slice method similur to .reverse()
# ---

class BasicPlan:
	can_stream = True
	can_download = True
	num_of_devices = 1
	has_SD = True
	has_HD = False
	has_UHD = False
	price = '$8.99'

# Write the classes for StandardPlan and PremiumPlan here!

class StandardPlan(BasicPlan):
	has_HD = True
	num_of_devices = 2
	price = '$12.99'

class PremiumPlan(StandardPlan):
	has_UHD = True
	num_of_devices = 4
	price = '$15.99'

#class inheritence
# ---

def parity(n):
	return "even" if n % 2 == 0 else "odd"

#return ['even', 'odd'][n % 2]
# ---
