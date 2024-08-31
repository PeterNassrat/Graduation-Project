class term_flag:
	def __init__(self):
		self._flag = False

	def switch(self):
		self._flag = True

	def get_flag(self):
		return self._flag
