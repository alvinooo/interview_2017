class LLNode(object):
	def __init__(self, value):
		self.next = None
		self.last = self

		if isinstance(value, list):
			self.value = value[0]
			for item in value[1:]:
				self.append_value(item)
		else:
			self.value = value

	def append_value(self, value):
		self.last.next = LLNode(value)
		self.last = self.last.next

	def append_node(self, node):
		self.last.next = node
		self.last = self.last.next

	def __str__(self):
		l = []
		curr = self
		while curr:
			l.append(curr.value)
			curr = curr.next
		return "{}".format(l)

if __name__ == "__main__":
	l = LLNode(1)
	for i in xrange(2, 10):
		l.append_value(i)
	print l
	print LLNode(range(1,10))