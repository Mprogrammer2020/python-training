''''
There are 52 cards in a deck of cards.

There are 4 persons in the game, i.e Daniel, Bryn, Phil and Justin

You have to distribute these 52 cards to these 4 persons in given way:

Give one card to Daniel, then two cards to Bryn, then three cards to Phil and finally four cards to Justin,

Then again five cards to Daniel, then six cards to Bryn, then seven cards to Phil and finally eight cards to Justin and so on until all the cards are distributed.

Finally display the number of cards each person has received.
Example output:
Daniel: 4 cards
Bryn: 10 cards
and so on.
'''
# total deck cards
total_cards = 52
# Players
players = ["Daniel", "Bryn", "Phil", "Justin"]

cards_per_player = [0 for _ in players]

# Distribute cards
num_cards = 1
while sum(cards_per_player) < total_cards:
  for i in range(len(players)):
    cards_per_player[i] += num_cards
    if sum(cards_per_player) >= total_cards:
      break
    num_cards += 1
#player received
for i in range(len(players)):
    print(f"{players[i]}: {cards_per_player[i]} cards")

         
     
                              
    
