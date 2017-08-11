from LLNode import *

head = LLNode(1)
loop = LLNode(2)
for i in xrange(3, 6):
	loop.append_value(i)
head.append_node(loop)
curr = loop
while curr.next:
	curr = curr.next
curr.next = loop

# curr = head
# for _ in xrange(10):
# 	print curr.value
# 	curr = curr.next

def loop_size(node):
	count = 1
	curr = node
	while curr.next != node:
		count += 1
		curr = curr.next
	return count

def loop_length(node):
	slow, fast = node, node.next
	while slow != fast:
		slow = slow.next
		fast = fast.next.next
	return loop_size(slow)

print loop_length(head)