#
# Copyright (c) James Quintero 2017
#

#determines best strategy for playing Ultimate Texas Holdem

import os.path
import time
import sys
import random


class UltimateTexasHoldem:

	#buy-in for $100
	bankroll=1000000
	#min-bet is $15
	bet=10
	#[0] = trips bet, [1] = ante bet, [2] = blind bet, [3] = play bet
	bets=[0,0,0,0]

	deck=[]
	board=[]
	player_hand=[]
	dealer_hand=[]

	#0 = high card
	#1 = pair
	#2 = 2-pair
	#3 = trips
	#4 = straight
	#5 = flush
	#6 = full house
	#7 = quads
	#8 = straight flush
	#9 = royal flush
	#[0] is hand strength, [1] is amount to multiply blind bet by
	blind_payout=[
	[0, 1], #pushes, 0/1 + 1
	[1, 1], #pushes, 0/1 + 1
	[2, 1], #pushes, 0/1 + 1
	[3, 1], #pushes, 0/1 + 1
	[4, 2], #pays 1 to 1, 1/1 + 1
	[5, 2.5], #pays 3 to 2, 3/2 + 1
	[6, 4], #pays 3 to 1, 3/1 + 1
	[7, 11], #pays 10 to 1, 10/1 + 1
	[8, 51], #pays 50 to 1, 50/1 + 1
	[9, 501] #pays 500 to 1, 500/1 + 1
	]

	trips_payout=[
	[0, 0], #loses
	[1, 0], #loses
	[2, 0], #loses
	[3, 4], #pays 3 to 1
	[4, 5], #pays 4 to 1
	[5, 8], #pays 7 to 1
	[6, 9], #pays 8 to 1
	[7, 31], #pays 30 to 1
	[8, 41], #pays 40 to 1 
	[9, 51] #pays 50 to 1 
	]


	


	def __init__(self):
		self.reset()
		self.board = ["","","","",""]
		self.player_hand = ["",""]
		self.dealer_hand = ["", ""]

	def reset(self):
		self.bankroll=1000000


	def run(self):

		print("Menu: ")
		print("1) Play")
		print("2) Simulate")
		print("3) Give best strategy")

		choice = int(input("Choice: "))


		#play
		if(choice==1):
			# play()
			print("Nothing here, yet")



		#simulate
		if(choice==2):
			# print("Nothing here, yet")
			# player_hands = [
			# ["14s", "14c"],
			# ["14s", "13c"],
			# ["14s", "12c"],
			# ["14s", "11c"],
			# ["14s", "10c"],
			# ["14s", "9c"],
			# ["14s", "8c"],
			# ["14s", "7c"],
			# ["14s", "6c"],
			# ["14s", "5c"],
			# ["14s", "4c"],
			# ["14s", "3c"],
			# ["14s", "2c"],

			# ["13s", "13c"],
			# ["13s", "12c"],
			# ["13s", "11c"],
			# ["13s", "10c"],
			# ["13s", "9c"],
			# ["13s", "8c"],
			# ["13s", "7c"],
			# ["13s", "6c"],
			# ["13s", "5c"],
			# ["13s", "4c"],
			# ["13s", "3c"],
			# ["13s", "2c"],

			# ["12s", "12c"],
			# ["12s", "11c"],
			# ["12s", "10c"],
			# ["12s", "9c"],
			# ["12s", "8c"],
			# ["12s", "7c"],
			# ["12s", "6c"],
			# ["12s", "5c"],
			# ["12s", "4c"],
			# ["12s", "3c"],
			# ["12s", "2c"],

			# ["11s", "11c"],
			# ["11s", "10c"],
			# ["11s", "9c"],
			# ["11s", "8c"],
			# ["11s", "7c"],
			# ["11s", "6c"],
			# ["11s", "5c"],
			# ["11s", "4c"],
			# ["11s", "3c"],
			# ["11s", "2c"],

			# ["10s", "10c"],
			# ["10s", "9c"],
			# ["10s", "8c"],
			# ["10s", "7c"],
			# ["10s", "6c"],
			# ["10s", "5c"],
			# ["10s", "4c"],
			# ["10s", "3c"],
			# ["10s", "2c"],

			# ["9s", "9c"],
			# ["9s", "8c"],
			# ["9s", "7c"],
			# ["9s", "6c"],
			# ["9s", "5c"],
			# ["9s", "4c"],
			# ["9s", "3c"],
			# ["9s", "2c"],

			# ["8s", "8c"],
			# ["8s", "7c"],
			# ["8s", "6c"],
			# ["8s", "5c"],
			# ["8s", "4c"],
			# ["8s", "3c"],
			# ["8s", "2c"],

			# ["7s", "7c"],
			# ["7s", "6c"],
			# ["7s", "5c"],
			# ["7s", "4c"],
			# ["7s", "3c"],
			# ["7s", "2c"],

			# ["6s", "6c"],
			# ["6s", "5c"],
			# ["6s", "4c"],
			# ["6s", "3c"],
			# ["6s", "2c"],

			# ["5s", "5c"],
			# ["5s", "4c"],
			# ["5s", "3c"],
			# ["5s", "2c"],

			# ["4s", "4c"],
			# ["4s", "3c"],
			# ["4s", "2c"],

			# ["3s", "3c"],
			# ["3s", "2c"]
			# ]

			# for x in range(0, len(player_hands)):
				# self.simulate(player_hands[x])
			self.simulate([])

		#print best strategy
		if(choice==3):
			print("Nothing here, yet")


	def simulate(self, player_hand):

		self.reset()

		num_player_wins = 0
		num_dealer_wins = 0
		num_pushes = 0

		num_runs=1000000
		# num_runs = 1

		# while(True):
		for x in range(0, num_runs):

			self.initialize_deck()

			#make bets
			self.initial_bets()

			
			#player gets random cards
			self.player_hand[0] = self.deck.pop()
			self.player_hand[1] = self.deck.pop()
			#player gets certain cards
			# self.player_hand = player_hand
			# self.deck.pop(self.deck.index(self.player_hand[0]))
			# self.deck.pop(self.deck.index(self.player_hand[1]))

			#deal rest of cards
			self.deal()

			# #player bets 4x
			# self.bets[3] = self.bet*4
			# self.bankroll -= self.bets[3]

			# self.print_current_state()


			dealer_hand_strength = self.determine_hand_strength(self.board, self.dealer_hand)
			player_hand_strength = self.determine_hand_strength(self.board, self.player_hand)

			winner = self.winner(player_hand_strength, dealer_hand_strength)

			#player won, so pay them
			if winner==1:
				num_player_wins += 1

				#pay player their trips
				trips_payout = self.trips_payout[player_hand_strength[0]][1]
				self.bankroll += self.bets[0]*trips_payout
				# print("Trips payout: $"+str(self.bets[0]*trips_payout))

				#if dealer has at least a pair pay player their ante
				if dealer_hand_strength[0]>0:
					self.bankroll += self.bets[1]*2
					# print("Ante payout: $"+str(self.bets[1]*2))
				#ante pushes
				else:
					self.bankroll += self.bets[1]
					# print("Ante payout: $"+str(self.bets[1]))


				#pay player their blind if they have straight or greater
				blind_payout = self.blind_payout[player_hand_strength[0]][1]
				self.bankroll += self.bets[2]*blind_payout
				# print("Blind payout: $"+str(self.bets[2]*blind_payout))

				#pay player their play bet
				self.bankroll += self.bets[3]*2
				# print("Play payout: $"+str(self.bets[3]*2))

			#dealer won, so bets
			elif winner==0:
				num_dealer_wins += 1
			
			#push
			else:
				num_pushes += 1


			if x!=0 and x%1000 == 0:
				print("Hand #"+str(x))



		print("Player hand: "+str(player_hand))
		self.print_current_state()

		print("Num player wins: "+str(num_player_wins))
		print("Num dealer wins: "+str(num_dealer_wins))
		print("Num pushes: "+str(num_pushes))

		print()
		print()




	#returns 1 if hand1 won, 0 if hand2 won, and -1 if split
	def winner(self, hand1_strength, hand2_strength):

		if hand1_strength[0]>hand2_strength[0]:
			return 1
		elif hand1_strength[0]<hand2_strength[0]:
			return 0
		#if same hand
		else:
			#if returned hand data doesn't include lists
			if hand1_strength[0]==8 or hand1_strength[0]==5 or hand1_strength[0]==4 or hand1_strength[0]==9:
				if hand1_strength[1]>hand2_strength[1]:
					return 1
				elif hand1_strength[1]<hand2_strength[1]:
					return 0
				else:
					return -1
			else:
				for x in range(0, len(hand1_strength[1])):
					if hand1_strength[1][x]>hand2_strength[1][x]:
						return 1
					elif hand1_strength[1][x]<hand2_strength[1][x]:
						return 0
				return -1



	# #tests self.determine_hand_strength()
	# def test(self):

	# 	#tests flush
	# 	board=["12c", "11c", "10c", "5s", "3c"]
	# 	hand = ["14c", "13c"]

	# 	hand_strength = self.determine_hand_strength(board, hand)
	# 	print(hand_strength)





	#places initial bets
	def initial_bets(self):

		#sets ante and blind to bet minimum
		# self.bets[0] = self.bet
		self.bets[0] = 0
		self.bets[1] = self.bet
		self.bets[2] = self.bet

		# self.bankroll -= self.bet*3
		self.bankroll -= self.bets[0]
		self.bankroll -= self.bets[1]
		self.bankroll -= self.bets[2]

	#deals cards
	def deal(self):

		#deals board first
		self.board[0] = self.deck.pop()
		self.board[1] = self.deck.pop()
		self.board[2] = self.deck.pop()
		self.board[3] = self.deck.pop()
		self.board[4] = self.deck.pop()

		self.dealer_hand[0] = self.deck.pop()
		self.dealer_hand[1] = self.deck.pop()




	#prints current state of the board and bets
	def print_current_state(self):
		print()

		print("Bankroll: $"+str(self.bankroll))
		print("Bet size: $"+str(self.bet))
		print()

		print("Trip bet: $"+str(self.bets[0]))
		print("Ante bet: $"+str(self.bets[1]))
		print("Bind bet: $"+str(self.bets[2]))
		print("Play bet: $"+str(self.bets[3]))
		print()

		print("Dealer hand: "+self.convert_card(self.dealer_hand[0])+","+self.convert_card(self.dealer_hand[1]))
		print("Board: "+self.convert_card(self.board[0])+","+self.convert_card(self.board[1])+","+self.convert_card(self.board[2])+","+self.convert_card(self.board[3])+","+self.convert_card(self.board[4]))
		print("player hand: "+self.convert_card(self.player_hand[0])+","+self.convert_card(self.player_hand[1]))
		print()

		dealer_hand_strength = self.determine_hand_strength(self.board, self.dealer_hand)
		print("Dealer hand strength: "+str(dealer_hand_strength))

		player_hand_strength = self.determine_hand_strength(self.board, self.player_hand)
		print("Player hand strength: "+str(player_hand_strength))

		print()






	def determine_hand_strength(self, board, hand):
		#0 = high card
		#1 = pair
		#2 = 2-pair
		#3 = trips
		#4 = straight
		#5 = flush
		#6 = full house
		#7 = quads
		#8 = straight flush
		#9 = royal flush

		#will return [#, [list of information like how high straight or flush is]]

		#starts at 0 spot (0 and 1 aren't used), and ends at Ace
		cards=[0]*15
		#spade, club, heart, diamond
		#list of cards that had that suit
		suits={"s": [], "c": [], "h": [], "d": []}

		#adds hand data to lists
		value1=int(hand[0][0:len(hand[0])-1])
		suit1=hand[0][-1:]
		value2=int(hand[1][0:len(hand[1])-1])
		suit2=hand[1][-1:]
		cards[value1]+=1
		suits[suit1].append(value1)
		cards[value2]+=1
		suits[suit2].append(value2)


		#adds board data to lists
		for x in range(0, len(board)):
			value=int(board[x][0:len(board[x])-1])
			suit=board[x][-1:]
			cards[value]+=1
			suits[suit].append(value)

		# print(hand)
		# print(board)
		# print(cards)
		# print(suits)

		has_straight=self.has_straight(cards)


		#if straight
		if has_straight[0]==True:
			str_height=has_straight[1]

			#if 5 of same suits in play and they're all in the straight
			for key in suits.keys():
				if len(suits[key])>=5 and str_height-4 in suits[key] and str_height-3 in suits[key] and str_height-2 in suits[key] and str_height-1 in suits[key] and str_height in suits[key]:
					
					#royal flush
					if str_height==14:
						return [9, 0]
					#straight flush
					return [8, str_height]

		#if quads
		if 4 in cards:
			quads=cards.index(4)

			#doesn't include quads in getting kicker
			cards[quads]=0

			#gets highest card in play
			kicker=self.get_kicker_indices(cards, 1)
			kicker=kicker[0]

			return [7, [quads, kicker] ]

		#if full house
		if (3 in cards and 2 in cards) or cards.count(3)==2:

			#gets highest 3 in play
			highest3=0
			for x in range(0, len(cards)):
				if cards[x]==3:
					highest3=x

			#doesn't include set of boat in getting other part
			cards[highest3]=0

			#gets highest 2 in play
			highest2=0
			for x in range(0, len(cards)):
				if cards[x]>=2:
					highest2=x

			#Aces of Kings full house will return [6, [14, 13]]
			return [6, [highest3, highest2]]

		#if flush
		for key in suits.keys():
			if len(suits[key])>=5:

				#returns highest player's flush if they have 2 of the suits
				if suit1==key and suit2==key:
					flush=max([value1, value2])
				#return player's flush if they have 1 of the suits or 0 if board plays
				if suit1==key:
					flush=value1
				elif suit2==key:
					flush=value2
				else:
					flush=0

				#returns highest card in flush
				return [5, flush]

		#if straight
		if has_straight[0]==True:
			return [4, has_straight[1]]

		#if trips
		if 3 in cards:
			trips=cards.index(3)

			#doesn't include trips in getting kicker
			cards[trips]=0

			#returns highest 2 cards not part of trips
			kickers=self.get_kicker_indices(cards, 2)

			return [3, [trips, kickers[0], kickers[1]]]

		#if 2 pair
		if cards.count(2)>=2:
			#gets highest two pair
			highest1=0
			highest2=0
			for x in range(0, len(cards)):
				if cards[x]==2:
					highest2=highest1
					highest1=x

			#doesn't include 2 pair in getting kicker
			cards[highest1]=0
			cards[highest2]=0

			#gets high card
			kicker=self.get_kicker_indices(cards, 1)
			kicker=kicker[0]

			return [2, [highest1, highest2, kicker]]

		#if regular pair
		if cards.count(2)==1:
			pair=cards.index(2)

			#doesn't include pair in getting kickers
			cards[pair]=0

			#get 3 other highest cards
			kickers=self.get_kicker_indices(cards, 3)

			values=[pair]
			for x in range(0, len(kickers)):
				if x<3:
					values.append(kickers[x])
			return [1, values]

		#if high card
		kickers=self.get_kicker_indices(cards, 5)
		return [0, kickers]




	#gets indicies for num_kickers
	def get_kicker_indices(self, temp_cards, num_kickers):
		temp=[]
		for x in range(len(temp_cards)-1, -1, -1):
			if temp_cards[x]!=0 and len(temp)<num_kickers:
				temp.append(x)
		return temp


	#returns [True, straight_height] if has straight
	def has_straight(self, cards):

		for x in range(2, len(cards)-4):
			if cards[x]>=1 and cards[x+1]>=1 and cards[x+2]>=1 and cards[x+3]>=1 and cards[x+4]>=1:
				return [True, x+4]

		#wheel straight
		if cards[2]>=1 and cards[3]>=1 and cards[4]>=1 and cards[5]>=1 and cards[14]>=1:
			return [True, 5]

		return [False, 0]


	def initialize_deck(self):

		#s = Spade
		#c = Club
		#h = Heart
		#d = Diamond
		deck=["2s","2c","2h","2d", 
		"3s","3c","3h","3d", 
		"4s","4c","4h","4d", 
		"5s","5c","5h","5d",
		"6s","6c","6h","6d",  
		"7s","7c","7h","7d",  
		"8s","8c","8h","8d",  
		"9s","9c","9h","9d",  
		"10s","10c","10h","10d",  
		"11s","11c","11h","11d",  
		"12s","12c","12h","12d",  
		"13s","13c","13h","13d",  
		"14s","14c","14h","14d"]

		#creates randomized list of cards
		random_deck=[]
		while len(deck)!=0:

			#gets random index
			random_index=random.randint(0, len(deck)-1)
			random_deck.append(deck[random_index])
			deck.pop(random_index)

		self.deck = random_deck

	#turns 12s into Qs
	def convert_card(self, card):

		before=["2s","2c","2h","2d", 
		"3s","3c","3h","3d", 
		"4s","4c","4h","4d", 
		"5s","5c","5h","5d",
		"6s","6c","6h","6d",  
		"7s","7c","7h","7d",  
		"8s","8c","8h","8d",  
		"9s","9c","9h","9d",  
		"10s","10c","10h","10d",  
		"11s","11c","11h","11d",  
		"12s","12c","12h","12d",  
		"13s","13c","13h","13d",  
		"14s","14c","14h","14d"]

		after=["2s","2c","2h","2d", 
		"3s","3c","3h","3d", 
		"4s","4c","4h","4d", 
		"5s","5c","5h","5d",
		"6s","6c","6h","6d",  
		"7s","7c","7h","7d",  
		"8s","8c","8h","8d",  
		"9s","9c","9h","9d",  
		"10s","10c","10h","10d",  
		"Js","Jc","Jh","Jd",  
		"Qs","Qc","Qh","Qd",  
		"Ks","Kc","Kh","Kd",  
		"As","Ac","Ah","Ad"]

		try:
			index = before.index(card)
		except Exception as error:
			return card

		return after[index]


	#converts 25.000000000000000001 to 25.0
	def convert_number(self, number):

		try:
			#compensates for 24.9999999 turning into 24.9 instead of 25.0
			temp=(number+0.001)*100
			temp=int(temp)/100
			new=int(number*100)/100

			if new<temp:
				new=temp

			return new
		except Exception as error:
			print("Error converting number: "+str(error))
			return number


if __name__=="__main__":
	UTH = UltimateTexasHoldem()
	UTH.run()