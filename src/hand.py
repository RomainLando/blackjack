class Hand:
	def __init__(self, dealer=False):
		self.cards = []
		self.value = 0
		self.dealer = dealer

	def add_card(self, card):
		if self.get_value() > 21:
			raise ValueError("Cannot add card to a bust hand")
		self.cards.append(card)
		self.calculate_value(card)

	def calculate_value(self, card):
		if card.value.isnumeric():
			self.add_to_value(int(card.value))
		elif card.value == "A":
			if self.get_value() > 10:
				self.add_to_value(1)
			else:
				if not self.dealer:
					print(f"Hand value: {self.get_value()}")
					chosen_value = input("Please choose the value of ace [1 / 11] ").lower()
					while chosen_value not in ["1", "11"]:
						chosen_value = input("Please enter '1' or '11' ").lower()
					if chosen_value in ["1", "11"]:
						self.add_to_value(int(chosen_value))
				else:
					self.add_to_value(11)
		else:
			self.add_to_value(10)

	def get_value(self):
		return self.value
	
	def add_to_value(self, num):
		self.value += num

	def dealer_initial_display(self):
		if self.value == 21:
			for card in self.cards:
				print(card)
			print(f"Hand value: {self.get_value()}")
			print()
		else:
			print("hidden")
			print(self.cards[1])
			print()

	def display(self):
		for card in self.cards:
			print(card)
		print(f"Hand value: {self.get_value()}")
		print()
