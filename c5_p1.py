input = raw_input("please input some words")
input = input.lower()
li = input.split(" ")


vowel = ["a","e","i","o","u"]
vowel_y = ["a","e","i","o","u","y"]
def ifvowel(word):
	if word[0] in vowel:
		word = word +"hay"
	return word
	
	
def ifqu(word):
	if word[0] == "q" and word[1] == "u":
		word = word[2:] + "quay"
	return word
	
def ifconsonant(word):
	i = 0
	if word[0] not in vowel:
		for a in word[1:]:
			if a not in vowel_y:
				i += 1
			else:
				break
		word = word[i+1:] +word[:i+1] +"ay"
	return word
	
def process(lis):
	newstr = ""
	new_lis = []
	for w in lis:
		w = ifvowel(w)
		w = ifqu(w)
		w = ifconsonant(w)
		new_lis.append(w)
	newstr = (" ").join(new_lis)
	return newstr
	
	
print process(li)
	
		