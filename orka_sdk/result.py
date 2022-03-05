class Result:

	def __init__(self, errors, data=None):
		self.data = data
		self.errors = errors
		if self.errors:
			self.success = False
		else:
			self.success = True
			