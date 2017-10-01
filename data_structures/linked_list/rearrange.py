from LLNode import LLNode

def find_middle(head):
	slow, fast = head, head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	return slow

def mid_to_head(head):
	mid = find_middle(head)
	prev_mid = head
	while prev_mid.next != mid:
		prev_mid = prev_mid.next
	prev_mid.next = mid.next
	mid.next = head
	return mid

l = LLNode(1)
for i in xrange(2, 6):
	l.append_value(i)
print l
print find_middle(l).value

print mid_to_head(l)