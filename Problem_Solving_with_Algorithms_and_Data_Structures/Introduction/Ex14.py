import random


class Card:

	suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
	value_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __str__(self):
		return f'{self.value} {self.suit}'


class Carddeck(Card):

	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(card)


	def shuffle(self):
		random.shuffle(self.card)

	def add(self):
		self.cards.append(card)

	def delete(self, card_del):
		self.cards.pop(card_del)

card = Card("3", "Diamonds")
print(card)