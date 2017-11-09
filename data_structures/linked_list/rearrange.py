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

def test_mid():
	l = LLNode(1)
	for i in xrange(2, 6):
		l.append_value(i)
	print l
	print find_middle(l).value

	print mid_to_head(l)

# test_mid()

def reverse(head):
	prev = None
	curr = head
	while curr:
		next = curr.next
		curr.next = prev
		prev = curr
		curr = next
	return prev

def rec_reverse(head):
	if not head or not head.next:
		return head
	else:
		tail = rec_reverse(head.next)
		head.next.next = head
		head.next = None
		return tail

def test_reverse():
	print reverse(LLNode(range(1,10)))
	print rec_reverse(LLNode(range(1,10)))

# test_reverse()

def odd_even(head):
	head1, head2 = head, head.next
	p1, p2 = head, head.next
	while p2 and p2.next:
		next1 = p1.next.next
		next2 = p2.next.next
		p1.next = p1.next.next
		p2.next = p2.next.next
		p1 = next1
		p2 = next2
	p1.next = head2
	return head1

def test_odd_even():
	print odd_even(LLNode(range(1,10)))

# test_odd_even()