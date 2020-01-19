from random import *
import copy


#Define a deck of cards
class Deck:

  def __init__(self, deckSizeI = 52, cardRangeI = 13, cardCountI = 4):
    self.cards = []
    self.deckSize = deckSizeI
    self.cardRange = cardRangeI
    self.cardCount = cardCountI
    cardsUsed = []
    for i in range(0, self.cardRange):
      cardsUsed.append(0)
    i = 0
    self.cards = [-1] * self.deckSize
    while i < self.deckSize:
      card = randint(0, self.cardRange - 1)
      if(cardsUsed[card] < self.cardCount):
        self.cards[i] = card
        i += 1
        cardsUsed[card] += 1
    return None
  
  
  def shuffle(self):
    cardsUsed = []
    for i in range(0, self.cardRange):
      cardsUsed.append(0)
    i = 0
    while i < self.deckSize:
      card = randint(0, self.cardRange - 1)
      if(cardsUsed[card] < self.cardCount):
        self.cards[i] = card
        i += 1
        cardsUsed[card] += 1
  
  
  def draw(self):
    self.deckSize -= 1
    return self.cards.pop(0)
    
  def discard(self, card):
    self.deckSize += 1
    self.cards.append(card)
    return
  
  
  def deal(self, cardCount, hands):
    for i in range(0, cardCount):
      for hand in hands:
        hand.add(self.draw())
        
 
 
 
#Define a hand of cards
class Hand:
  
  def __init__(self, cards = []):
    self.cards = copy.copy(cards)
    self.handSize = 0
    return None
  
  def add(self, card):
    self.handSize += 1
    self.cards.append(card)
  
  
  def remove(self, cardNum):
    self.handSize -= 1
    return self.cards.pop(cardNum)
  
  
  def sort(self):
    self.cards.sort()
    
    
  def getCards(self):
    return self.cards
    
    
  def getDistrib(self):
    distrib = Distrib(self.cards)
    return distrib
    
  def index(self, card):
    return self.cards.index(card)
    
  def getSize(self):
    return self.handSize
  
  
  
  
#Define an object that can be used to perform statistical analysis on a hand of cards
class Distrib:
  
  def __init__(self, cards):
    self.cards = []
    self.count = []
    for card in cards:
      self.append(card)
    return None
    
  
  def append(self, card):
    if card in self.cards:
      self.count[self.cards.index(card)] += 1
    else:
      self.cards.append(card)
      self.count.append(1)
      
   
  def getCount(self, card):
    return self.count[self.cards.index(card)]
     
   
  def getMax(self):
    return self.cards[self.count.index(max(self.count))]
      
      
  def getMin(self):
    return self.cards[self.count.index(min(self.count))]

      
      
#Define the rules and process for a game of spoons
class SpoonsGame:
  
  def __init__(self, playersI = 2, handSizeI = 4):
    self.hands = []
    self.players = playersI
    self.handSize = handSizeI
    self.roundCount = 0
    self.deckSize = 52
    self.handSize = 4
    self.roundCount = 0
    self.deck = Deck(self.deckSize)
    self.hands = [Hand() for i in range(0, self.players)]
    self.deck.deal(self.handSize, self.hands)
    
    return None
    
    
  def playTurn(self, hand, card):
    discard = card
    if card in hand.getCards():
      if hand.getDistrib().getCount(hand.getDistrib().getMax()) <= self.handSize / 2 or hand.getDistrib().getMax() == card:
        tempHand = Hand(copy.copy(hand.getCards()))
        while card in tempHand.getCards():
          tempHand.remove(tempHand.index(card))
        discard = hand.remove(hand.index(tempHand.getDistrib().getMin()))
        hand.add(card)
    return discard
  
  
  def playRound(self):
    self.roundCount += 1
    nextCard = self.deck.draw()
    handCards = 0
    for hand in self.hands:
      handCards += hand.getSize()
      nextCard = self.playTurn(hand, nextCard)
      if hand.getDistrib().getCount(hand.getDistrib().getMax()) == self.handSize:
        return self.hands.index(hand)
    self.deck.discard(nextCard)
    if self.roundCount % (self.deckSize - handCards) == 0:
      self.deck.shuffle()
    return -1
  
  
  def playGame(self):
    winner = self.playRound()
    while winner == -1:
      winner = self.playRound()
    return winner
      
      
  def getRoundCount(self):
    return self.roundCount
      


#Set simulation variables
players = int(input("Players: "))
rounds = int(input("Rounds: "))
wins = []

#Initialize win counter
for i in range(0, players):
  wins.append(0)

#Run simulation
for x in range(0, rounds):
  game = SpoonsGame(players)
  wins[game.playGame()] += 1




#Output block
print("\n")
print("Statistics from " + str(rounds) + " rounds of spoons with " + str(players) + " players:")
print("")
print("  Player | Win Rate")
print("  -------+---------")
for p in range(0, players):
  print("      " + str(p + 1).rjust(2, " ") + " | " + ("{0:." + str(len(str(rounds)) - 3) + "f}").format(((float(wins[p])/float(rounds))*100)).rjust(len(str(rounds)), " ") + "%")
print("\n")
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
  
