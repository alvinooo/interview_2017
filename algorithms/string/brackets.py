def max_nested_depth(s):
	stack = []
	max_depth, curr_depth = 0, 0
	for c in s:
		if c == ")" and len(stack) == 0:
			return -1
		elif c == ")":
			stack.pop()
			curr_depth -= 1
		elif c == "(":
			stack.append(c)
			curr_depth += 1
		max_depth = max(max_depth, curr_depth)
	if len(stack) != 0:
		return -1
	return max_depth

print max_nested_depth("( ((X)) (((Y))) )")
print max_nested_depth("( a(b) (c) (d(e(f)g)h) I (j(k)l)m)")
print max_nested_depth("( p((q)) ((s)t) )")
print max_nested_depth("")
print max_nested_depth("b) (c) ()")
print max_nested_depth("(b) ((c) ()")