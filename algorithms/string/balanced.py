def reversal_count(s):
	if len(s) % 2 == 1:
		return -1
	unbalanced = []
	for c in s:
		if len(unbalanced) != 0 and c == "}" and unbalanced[-1] == "{":
			unbalanced.pop()
		else:
			unbalanced.append(c)
	open_count = 0
	while len(unbalanced) > 0 and unbalanced[-1] == "{":
		open_count += 1


print reversal_count("}{") # 2
print reversal_count("{{{")
print reversal_count("{{{{") # 2
print reversal_count("{{{{}}") # 1
print reversal_count("}{{}}{{{") # 3