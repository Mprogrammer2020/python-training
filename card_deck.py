'''But I've one issue 
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


total_cards = 52
players = ["Daniel", "Bryn", "Phil", "Justin"]

cards_per_player = [0 for _ in players]

# Distribute cards
def distribute_cards(total_cards, cards_per_player):
    num_cards = 1
    while total_cards > 0:
        for i in range(len(players)):
            if total_cards >= num_cards:
                cards_per_player[i] += num_cards
                total_cards -= num_cards
            else:
                  # give the remaining cards
                cards_per_player[i] += total_cards
                total_cards = 0
                break
            num_cards += 1 
    return cards_per_player
cards_per_player = distribute_cards(total_cards, cards_per_player)

for i in range(len(players)):
    print(f"{players[i]} received {cards_per_player[i]} cards.")
