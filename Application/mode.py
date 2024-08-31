class mode:
	def __init__(self, mode = 0):
		self._mode = mode
	def change(self, mode):
		self._mode = mode
	def get(self):
		return self._mode
