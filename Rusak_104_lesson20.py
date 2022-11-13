# Домашнее задание
card_rang = ['туз', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король']
card_suit = ['треф', 'бубен', 'червей', 'пик']

card_deck = [i + ' ' + x for i in card_rang for x in card_suit]  # Список содежащий название всех 52х карт в коложе
cardDeck = iter(card_deck)  # Итератор колоды карт

print(cardDeck)

for i in range(53):  # Проверка циклом, выполняется ли условие задания
    print(next(cardDeck))
