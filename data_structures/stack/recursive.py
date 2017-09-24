def _remove_bottom(stack):
	if len(stack) != 0:
		top = stack.pop()
		bottom = _remove_bottom(stack)
		if bottom:
			stack.append(top)
		return bottom if bottom else top

def reverse(stack):
	if len(stack) == 0:
		return
	else:
		bottom = _remove_bottom(stack)
		reverse(stack)
		stack.append(bottom)

stack = [1,2,3,4,5]
reverse(stack)
print stack
# stack = [1,2,3]
# print _remove_bottom(stack)
# print stack