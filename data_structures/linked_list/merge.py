from LLNode import *

l1 = LLNode([5, 10, 15])
l2 = LLNode([2, 3, 20])

def rec_merge_sorted(l1, l2):
	if not l1:
		return l2
	if not l2:
		return l1
	if l1.value < l2.value:
		head = l1
		head.next = rec_merge_sorted(l1.next, l2)
		return head
	else:
		head = l2
		head.next = rec_merge_sorted(l1, l2.next)
		return head

print rec_merge_sorted(l1, l2)