def hello_world(num):
	if num % 3 == 0 and num % 5 == 0:
		return "Hello World"
	elif num % 5 == 0:
		return "World"
	elif num % 3 == 0:
		return "Hello"

# ---

def hash_plus_count(txt):
	lstCount = [txt.count("#"),txt.count("+")]
	return lstCount

# ---

def reverse(lst):
	lst.reverse()
	return lst

#return lst.reverse(), throws error
#return lst[::-1], would work for one liner (slice method)
# ---

def reverse_case(txt):
	return txt.swapcase()

# ---

def md_format(word, style):
	styleObj = {
	"b": "**{}**",
	"i": "_{}_",
	"c": "`{}`",
	"s": "~~{}~~"
	}

	return styleObj[style].format(word)

# ---

def km_to_miles(kilometers):
	return round(kilometers*0.621371, 5)

# ---

def find_digit_amount(num):
	return len(str(num))

# ---
