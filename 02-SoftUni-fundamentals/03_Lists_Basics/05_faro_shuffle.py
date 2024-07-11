def faro_shuffle(deck, shuffles):
    for _ in range(shuffles):
        half = len(deck) // 2
        left_half = deck[:half]
        right_half = deck[half:]
        deck = [card for pair in zip(left_half, right_half) for card in pair]
    return deck


cards = input().split()
shuffle_count = int(input())

shuffled_deck = faro_shuffle(cards, shuffle_count)

print(shuffled_deck)
