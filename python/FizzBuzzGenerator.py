class FizzBuzzGenerator:
    def validateInput(self,input):
		if type(input) == int:
			if input > 0:
				return True
			else:
				return None
		else:
			return None

    def fizzBuzzGenerator(self,input):
        if self.validateInput(input):
            pass
        