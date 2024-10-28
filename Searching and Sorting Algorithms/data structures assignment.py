from array import array
from _ctypes import PyObj_FromPtr
from datetime import datetime
from time import sleep

class application:
	'''
	This class is used for declaring and displaying individual applications.
	This is also where the queue to store the applications is defined.
	'''
	def __init__(self, full_name, national_id, d_o_b, applic_date, amount, purpose):
		self.full_name = full_name
		self.national_id = national_id
		self.d_o_b = d_o_b
		self.applic_date = applic_date
		self.amount = amount
		self.purpose = purpose

	def display_details(self): # Displays the details for each application
		spaces_left, spaces_right = 20 * "-", 30 * "-"
		print("+" + spaces_left + "+" + spaces_right + "+")
		print("|{:<20}|{:<30}|".format("Full Name", self.full_name))
		print("|" + spaces_left + "+" + spaces_right + "|")
		print("|{:<20}|{:<30}|".format("National ID", self.national_id))
		print("|" + spaces_left + "+" + spaces_right + "|")
		print("|{:<20}|{:<30}|".format("Date of Birth", self.d_o_b.strftime("%a %d-%m-%Y")))
		print("|" + spaces_left + "+" + spaces_right + "|")
		print("|{:<20}|{:<30}|".format("Application Date", self.applic_date.strftime("%a %d-%m-%Y")))
		print("|" + spaces_left + "+" + spaces_right + "|")
		print("|{:<20}|{:<30}|".format("Amount", self.amount))
		print("|" + spaces_left + "+" + spaces_right + "|")
		print("|{:<20}|{:<30}|".format("Purpose", self.purpose))
		print("+" + spaces_left + "+" + spaces_right + "+")
		print(end="\n\n")

	class application_queue:
		def __init__(self):
			self.queue = array('Q') # Stores the addresses of application objects in memory

		def size(self):
			return len(self.queue)

		def empty(self):
			return self.size() == 0

		def enqueue(self, application):
			self.queue.append(id(application))

		def dequeue(self):
			if not self.empty():
				return PyObj_FromPtr(self.queue.pop(0))
			else:
				print("self queue is empty")

		def peek(self):
			if not self.empty():
				return PyObj_FromPtr(self.queue[0])
			else:
				print("The queue is empty")


class my_binary_search_tree:
	def __init__(self):
		# The the my_binary_search_tree class serves as the root node
		# Sorts by National_ID
		self.application = None
		self.left_sub_tree = None
		self.right_sub_tree = None

	def insert(self, application):
		if self.empty():
			self.application = application
		else:
			current_node, inserted = self, False
			while not inserted:
				if application.national_id > current_node.application.national_id and not current_node.right_sub_tree:
					current_node.right_sub_tree = node(application)
					inserted = True
				elif application.national_id <= current_node.application.national_id and not current_node.left_sub_tree:
					current_node.left_sub_tree = node(application)
					inserted = True
				elif application.national_id > current_node.application.national_id:
					current_node = current_node.right_sub_tree
				elif application.national_id <= current_node.application.national_id:
					current_node = current_node.left_sub_tree

	def search(self, national_id):
		current_node = self
		while current_node:
			if current_node.application.national_id == national_id:
				return current_node.application
			if national_id > current_node.application.national_id:
				current_node = current_node.right_sub_tree
			else:
				current_node = current_node.left_sub_tree
		else:
			print("\nThis application is not in our System.\n")

	def get_apps(self, apps, current_node):
		if current_node.application:
			apps.append(current_node.application)
			if current_node.left_sub_tree:
				self.get_apps(apps, current_node.left_sub_tree)
			if current_node.right_sub_tree:
				self.get_apps(apps, current_node.right_sub_tree)

	def delete_node(self, national_id):
		apps = []
		self.get_apps(apps, self)
		self.application = None
		self.left_sub_tree = None
		self.right_sub_tree = None
		for app in apps:
			if not national_id == app.national_id:
				self.insert(app)

	def empty(self):
		return self.application is None


class node:
	# The node for the binary search tree
	def __init__(self, application):
	 	self.application = application
	 	self.left_sub_tree = None
	 	self.right_sub_tree = None


class application_dao:
	"""
	This class contains the CRUD operations for the my_binary_search_tree class
	The application class and the application_queue class.
	C - Creation, R - Retrieval, U - Updating, D - Deletion
	"""
	def __init__(self):
		self.queue = application.application_queue()
		self.application_tree = my_binary_search_tree()

	def add_application(self):
		#Posssible purposes
		purposes = {1: "Fees", 2: "Business", 3:"Car", 4:"Building"}
		#Entering the details
		full_name = input("Enter your Full Name: ")
		national_id = input("Enter your National ID without the hyphen(-): ")
		d_o_b = input("Enter your Date of Birth in the format YYYY-MM-DD: ").split("-")
		d_o_b = datetime(*list(map(int, d_o_b)))
		applic_date = datetime.now()
		amount = int(input("Enter the amount: "))
		purpose = purposes[int(input("""What's the purpose of the loan: 
		1. {}
		2. {}
		3. {}
		4. {}   : """.format(purposes[1], purposes[2], purposes[3], purposes[4])))]
		# Creating an application object and putting it in the queue and tree
		new = application(full_name, national_id, d_o_b, applic_date, amount, purpose)
		self.queue.enqueue(new)
		self.application_tree.insert(new)

	def del_application(self):
		app = self.queue.dequeue()
		self.application_tree.delete_node(app.national_id)

	def get_apps(self):
		self.application_tree.get_apps(apps := [], self.application_tree)
		return apps

	def show_applications(self, apps):
		if apps:
			for app in apps:
				app.display_details()
				sleep(0.5)
		else:
			print("\nThere are no applications in our System\n")

	# Sorting Algorithms
	def sort_by_amount(self):
		apps = self.get_apps()
		done = False
		while not done:
			done = True
			for i in range(len(apps) - 1):
				if apps[i].amount > apps[i + 1].amount:
					apps[i], apps[i + 1] = apps[i + 1], apps[i]
					done = False
		return apps

	def sort_by_national_id(self):
		# This code uses bubble sort
		apps = self.get_apps()
		done = False
		while not done:
			done = True
			for i in range(len(apps) - 1):
				if apps[i].national_id > apps[i + 1].national_id:
					apps[i], apps[i + 1] = apps[i + 1], apps[i]
					done = False
		return apps
	
	def partition(self, array, start, end):
		# The acompanying partition methpd for the quick_sort
		pivot = array[end].applic_date.strftime("%Y%m%d%X")
		p_index = start
		for i in range(start, end):
			if array[i].applic_date.strftime("%Y%m%d%X") > pivot:
				array[i], array[p_index] = array[p_index], array[i]
				p_index += 1
		array[p_index], array[end] = array[end], array[p_index]
		return p_index

	def sort_by_applic_date(self, array, start, end):
		# This code uses quicksort
		if start < end:
			index = self.partition(array, start, end)
			self.sort_by_applic_date(array, start, index - 1)
			self.sort_by_applic_date(array, index + 1, end)

	#Searching Algorithms
	def search_by_national_id_1(self, national_id):
		'''Search uses binary Search'''
		apps = self.sort_by_national_id()
		start, end = 0, self.queue.size()
		while start <= end:
			mid = (start + end) // 2
			if apps[mid].national_id == national_id:
				return apps[mid].display_details()
			elif national_id > apps[mid].national_id:
				start = mid + 1
			else:
				end = mid - 1
		else:
			print("There is no application with that National ID in our system.")

	def search_by_national_id_2(self, national_id):
		# Faster search using the binary search tree
		return self.application_tree.search(national_id).display_details()


def message() -> int:
	print("\nHere are your options: ")
	print("1. Add an application")
	print("2. Remove an application")
	print("3. Display the applications by Application Date")
	print("4. Display the applications by Loan Amount")
	print("5. Search for an application by National ID")
	print("6. View the next application to be processed\n")
	return int(input("Enter your option here: "))

def main():
	my_app = application_dao()
	while answer := input("Do you want to continue using the Application (Y or N): ").upper() == 'Y':
		try:
			option = message()
			if option == 1:
				my_app.add_application()
			elif option == 2:
				my_app.del_application()
			elif option == 3:
				my_app.sort_by_applic_date(apps := my_app.get_apps(), 0, len(apps) - 1)
				my_app.show_applications(apps)
			elif option == 4:
				my_app.show_applications(my_app.sort_by_amount())
			elif option == 5:
				option_2 = int(input("Do you want to serach with Binary Search (1) or from Binary Search tree (2): "))
				if option_2 == 1:
					my_app.search_by_national_id_2(input("\nEnter the National ID for the search: "))
				elif option_2 == 2:
					my_app.search_by_national_id_2(input("\nEnter the National ID for the search: "))
				else:
					raise Exception("That's not a Valid option")
			elif option == 6:
				my_app.queue.peek().display_details()
		except Exception as e:
			print("\n", e)
			sleep(0.3)
			print("\nYou must have entered some data incorrectly")
			print("As a result the action you wanted will not be executed\nYou can try again\n")
			sleep(0.3)

main()
