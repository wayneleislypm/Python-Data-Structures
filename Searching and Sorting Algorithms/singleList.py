class SingleList(object):
	class Node(object):
		def __init__(self,data,next):
			self.data = data
			self.next = next
			
	def __init__(self):
			self.head = None
			self.tail = None
			
	def show(self):
			print('showing list data: ')
			current_node = self.head
			while current_node is not None:
				print(current_node.data, '->')
				current_node = current_node.next
				#print(None)
				
	def insert(self, data):
			if self.head == None:
				self.head = self.Node(data,None)
				self.tail = self.head
			elif self.tail == self.head:
				self.tail = self.Node(data, None)
				self.head.next = self.tail	
			else:
				current = self.Node(data, None)
				self.tail.next = current
				self.tail = current
				
	def remove(self, node_value):
				current_node = self.head
				previous_node = None
				while current_node is not None:
					if current_node.data == node_value:
						if previous_node is not None:
							previous_node.next = current_node.next
						else:
							self.head = current_node.next
					previous_node = current_node
					current_node = current_node.next
	def search(self, k):
				p = self.head
				if p != None:
					while p.next != None:
						if p.data == k:
							return True
						p = p.next
					if (p.data == k):
						return False
				return False

s = SingleList()
s.insert(31)
s.insert(2)
s.insert(3)
s.show()
print(s.search(31))
print(s.search(300))
s.remove(3)
s.show()
				