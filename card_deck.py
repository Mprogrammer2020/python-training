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
#  cards each person has
daniel_cards = 0
bryn_cards = 0
phil_cards = 0
justin_cards = 0
#cards to give to each person
daniel_to_give =1
bryn_to_give = 2
phil_to_give = 3
justin_to_give = 4

# total number of cards
total_cards = 52
# Distribute the cards
while total_cards > 0:
    # Give cards to Daniel
    if total_cards >= daniel_to_give:
        daniel_cards += daniel_to_give
        total_cards -= daniel_to_give
    else:
        daniel_cards += total_cards
        total_cards = 0
    # Give cards to Bryn
    if total_cards > 0 and total_cards >= bryn_to_give:
        bryn_cards += bryn_to_give
        total_cards -= bryn_to_give
    elif total_cards > 0:
        bryn_cards += total_cards
        total_cards = 0
        
    # Give cards to Phil
    if total_cards > 0 and total_cards >= phil_to_give:
        phil_cards += phil_to_give
        total_cards -= phil_to_give
    elif total_cards > 0:
        phil_cards += total_cards
        total_cards = 0

    # Give cards to Justin
    if total_cards > 0 and total_cards >= justin_to_give:
        justin_cards += justin_to_give
        total_cards -= justin_to_give
    elif total_cards > 0:
        justin_cards += total_cards
        total_cards = 0

print("Daniel:", daniel_cards)
print("Bryn:", bryn_cards)
print("Phil:", phil_cards)
print("Justin:", justin_cards)

         
     
                              
    
