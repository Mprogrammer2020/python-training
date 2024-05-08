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

def distribute_cards(): 
    daniel_cards = 0
    bryn_cards = 0
    phil_cards = 0
    justin_cards = 0
    #  card count
    card_count = 1

    # Distribut cards every person
    while card_count <= 36:
        daniel_cards += 1
        card_count += 1
        
        if card_count <= 36:
            bryn_cards += 2
            card_count += 2
            
        if card_count <= 36:
            phil_cards += 3
            card_count += 3
            
        if card_count <= 36:
            justin_cards += 4
            card_count += 4
            
        if card_count <= 36:
           daniel_cards += 5
           card_count += 5
        
        if card_count <= 36:
            bryn_cards += 6
            card_count += 6
            
        if card_count <= 36:
            phil_cards += 7
            card_count += 7
            
        if card_count <= 36:
            justin_cards += 8
            card_count += 8             
    #add remaining cards to Daniel
    daniel_cards += 16
   
    print("Daniel:", daniel_cards)
    print("Bryn:", bryn_cards)
    print("Phil:", phil_cards)
    print("Justin:", justin_cards)
distribute_cards()

         
     
                              
    
