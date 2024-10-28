class Node(object):
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None
		
	def insert(self, data):
		if self.value == data:
			return False
		elif self.value > data:
			if self.left:
				return self.left.insert(data)
			else:
				self.left = Node(data)
				return True
		else:
			if self.right:
				return self.right.insert(data)
			else:
				self.right = Node(data)
				return True
	def find(self, data):
		if self.value == data:
			return True
		elif self.value > data:
			if self.left:
				return self.left.find(data)
			else:
				return True
		else:
			if self.right:
				return self.right.find(data)
			else:
				return False 
				
	def preorder(self):
		if self:
			print(str(self.value))
			if self.left:
				self.left.preorder()
			if self.right:
				self.right.preorder()
				
	def postorder(self):
		if self:
			if self.left:
				self.left.postorder()
			if self.right:
				self.right.postorder()
			print(str(self.value))
			
	def inorder(self):
			if self:
				if self.left:
					self.left.inorder()
				print(str(self.value))
				if self.right:
					self.right.inorder()
					
	def _findMin(self, parent):
					if self.left:
						return self.left._findMin(self)
					else:
						return [parent, self]
						
	def delete(self, data):
			if self.value == data:
				if self.right and self.left:
					[psucc, succ] = self.right._findMin(self)
					if psucc.left == succ:
						psucc.left == succ.right
					else:
						psucc.right == succ.right
					succ.left = self.left
					succ.right = self.right
					return succ
				else:
						if self.left:
							return self.left
						else:
							return self.right
			else:
						if self.value >data:
							if self.left:
								self.left = self.left.delete(data)
						else:
							if self.right:
								self.rght = self.right.delete(data)
			return self
			
class Tree:
			def __init__(self):
				self.root = None
			
			def insert(self, data):
				if self.root:
					return self.root.insert(data)
				else:
					self.root = Node(data)
					return True
					
			def  find(self, data):
				if self.root:
					return self.root.find(data)
				else:
					return False
			
			def postorder(self):
				print('postorder')			
				self.root.postorder()
			
			def preorder(self):
				print('preorder')
				self.root.preorder()
				
			def inorder(self):
				print('inorder')
				self.root.inorder()
				
			def delete(self, data):
				if self.root:
					self.root = self.root.delete(data)
				
			def show(self):
					print(self.root)
					
m = Tree()
m.insert(87)
m.insert(99)
m.insert(90)
m.insert(120)
m.insert(900)
m.insert(70)
m.insert(10)
m.insert(50)
print(m.insert(77))
print(m.delete(70))
m.show()
#print(m.find(70))
#m.preorder()
#m.postorder()
#m.inorder()