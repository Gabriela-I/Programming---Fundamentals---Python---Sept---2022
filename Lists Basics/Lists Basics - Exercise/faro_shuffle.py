deck_of_cards = input().split()

number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    final_deck = []
    left_side = deck_of_cards[:(len(deck_of_cards)//2)]
    right_side = deck_of_cards[(len(deck_of_cards)//2):]
    for index in range(len(left_side)):
        final_deck.append(left_side[index])
        final_deck.append(right_side[index])
    deck_of_cards = final_deck
print(deck_of_cards)



