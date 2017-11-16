from DLLNode import DLLNode

class LRUCache(object):
	def __init__(self, max_capacity):
		self.max_capacity = max_capacity
		self.cache = {}
		self.eviction_list = None
		self.curr_capacity = 0

	def put(self, key, value):
		node = DLLNode(value)
		if self.curr_capacity >= self.max_capacity:
			evicted_value = self.eviction_list.value
			self.eviction_list = self.eviction_list.next
			self.cache.pop(evicted_value)
			self.curr_capacity -= 1

		if self.eviction_list:
			self.eviction_list.append(node)
		else:
			self.eviction_list = node

		self.curr_capacity += 1
		self.cache[key] = node
		# print self.eviction_list, self.cache

	def get(self, key):
		if key not in self.cache:
			return -1
		node = self.cache[key]
		if self.eviction_list == node:
			self.eviction_list = node.next
		if node.prev:
			node.prev.next = node.next
		if node.next:
			node.next.prev = node.prev
		self.eviction_list.append(key)
		return node.value

def test_lru_cache():
	cache = LRUCache(2)
	cache.put(1, 1)
	cache.put(2, 2)
	print cache.get(1)	# returns 1
	cache.put(3, 3)	# evicts key 2
	print cache.get(2)	# returns -1 (not found)
	cache.put(4, 4)	# evicts key 1
	print cache.get(1)	# returns -1 (not found)
	print cache.get(3)	# returns 3
	print cache.get(4)	# returns 4

test_lru_cache()