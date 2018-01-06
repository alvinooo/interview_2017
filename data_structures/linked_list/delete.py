# http://www.geeksforgeeks.org/remove-duplicates-from-a-sorted-linked-list/

from LLNode import LLNode

def remove_duplicates(sorted_list):
	if not sorted_list:
		return
	curr_node = sorted_list
	while curr_node.next:
		if curr_node.value == curr_node.next.value:
			curr_node.next = curr_node.next.next
		else:
			curr_node = curr_node.next

def test_remove_duplicates():
	l = LLNode([11,11,11,21,43,43,60])
	remove_duplicates(l)
	print l

# test_remove_duplicates()