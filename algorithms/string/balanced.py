def reversal_count(s):
	if len(s) % 2 == 1:
		return -1
	unbalanced = []
	for c in s:
		if len(unbalanced) != 0 and c == "}" and unbalanced[-1] == "{":
			unbalanced.pop()
		else:
			unbalanced.append(c)
	unbalanced_length = len(unbalanced)
	open_count = 0
	while len(unbalanced) > 0 and unbalanced[-1] == "{":
		open_count += 1
		unbalanced.pop()
	return min(open_count, unbalanced_length - open_count) + unbalanced_length / 2

# print reversal_count("}{") # 2
# print reversal_count("{{{")
# print reversal_count("{{{{") # 2
# print reversal_count("{{{{}}") # 1
# print reversal_count("}{{}}{{{") # 3

def reversal_count_constant_space(s):
	if len(s) % 2 == 1:
		return -1
	reversals = 0
	segment = 0

	for c in s:
		if c == '}':
			if segment > 0:
				segment -= 1
			else:
				reversals += 1
				segment = 1
		else:
			segment += 1
	return reversals + segment / 2

print reversal_count_constant_space("}{") # 2
print reversal_count_constant_space("{{{")
print reversal_count_constant_space("{{{{") # 2
print reversal_count_constant_space("{{{{}}") # 1
print reversal_count_constant_space("}{{}}{{{") # 3