from LLNode import LLNode

# https://gist.github.com/nichochar/87e18f9eb72f114853eb
class DLLNode(LLNode):
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None
		self.last = self

		if isinstance(value, list):
			self.value = value[0]
			for item in value[1:]:
				self.append(item)

	def dequeue(self):
		head = self
		self = self.next
		return head

	def append(self, element):
		if isinstance(element, DLLNode):
			node = element
		else:
			node = DLLNode(element)
		self.last.next = node
		node.prev = self.last
		self.last = self.last.next

	def remove(self, node):
		if self == node:
			self = self.next
		if node.prev:
			node.prev.next = node.next
		if node.next:
			node.next.prev = node.prev
		return self

	def __str__(self):
		l = []
		curr = self
		while curr:
			l.append(curr.value)
			curr = curr.next
		return "{}".format(l)

if __name__ == "__main__":
	l = DLLNode(1)
	for i in xrange(2, 10):
		l.append(i)
	# print l
	# print DLLNode(range(1,10))
	print l.dequeue()
	print l