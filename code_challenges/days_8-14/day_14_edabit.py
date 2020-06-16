def reverse_title(txt):
	txt.upper()
	arrTxt = txt.split(" ")
	finalArr = []
	for i in arrTxt:
		finalArr.append(i[0].lower() + i[1:len(i)].upper())
	return " ".join(finalArr)

#return txt.title().swapcase()
# ---

def number_squares(n):
    i = 1
    sumTotal = 0
    while i < n+1:
        sumTotal += i*i
        i += 1
    return sumTotal

# ---

def repetition(txt, n):
	return txt*n

# ---

def unlucky_13(nums):
	filtArr = filter(lambda x: x%13 != 0, nums)
	return list(filtArr)

# ---

def first_last(name):
  return name[0] + name[-1]

# ---

def after_n_months(year, month):
	if year == None:
		return "year missing"
	if month == None:
		return "month missing"
	yearsAdd = month//12
	return year + yearsAdd

# ---
