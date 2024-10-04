import cards
import random


def check_blackjack(cards):
    return sum(cards) == 21

def determine_winner(user_cards, dealer_cards):
    print('=' * 35)
    user_sum = sum(user_cards)
    dealer_sum = sum(dealer_cards)
    
    if user_sum == 21 and dealer_sum != 21:
        print('YOU GOT A BLACKJACK!, YOU WIN!')
    elif dealer_sum == 21 and user_sum != 21:
        print('YOU LOSE! DEALER GOT A BLACKJACK!')
    elif dealer_sum > 21:
        print('DEALER WENT OVER 21. YOU WIN!')
    elif user_sum > 21:
        print('YOU WENT OVER 21. YOU LOSE!')
    elif user_sum > dealer_sum:
        print('YOU WIN!')
    elif dealer_sum > user_sum:
        print('YOU LOSE!')
    else:
        print('IT\'S A DRAW!')

    print(f'Your cards: {user_cards}')
    print(f'Dealer cards: {dealer_cards}')
    print(f'Your sum: {user_sum}')
    print(f'Dealer sum: {dealer_sum}')
    print('=' * 35)

def play_again():
    if input('Do you want to play again? (y/n): ') == 'y':
        main()
    exit()


def main():
    print('=' * 35)
    user_cards = [random.choice(cards.cards) for _ in range(2)]
    dealer_cards = [random.choice(cards.cards) for _ in range(2)]

    print(f'Your cards: {user_cards}')
    print(f'Dealer cards: {dealer_cards[0]}, _')

    if check_blackjack(user_cards) and not check_blackjack(dealer_cards):
        print('You got a blackjack!')
        determine_winner(user_cards, dealer_cards)

    while True:
        if input('Do you want to hit or stand? (h/s): ').lower() == 'h':
            user_cards.append(random.choice(cards.cards))
            print(f'Your cards: {user_cards}')
            user_sum = sum(user_cards)
            print(f'Your sum: {user_sum}')
            if user_sum > 21 and 11 in user_cards:
                print('Converted 11 to 1')
                user_cards[user_cards.index(11)] = 1
                print(f'Your cards: {user_cards}')
            elif user_sum >= 21:
                break
        else:
            break

    if sum(user_cards) <= 21:
        while sum(dealer_cards) < 17:
            dealer_cards.append(random.choice(cards.cards))

    determine_winner(user_cards, dealer_cards)
    play_again()


if __name__ == '__main__':
    print('=' * 35)
    print('WELCOME TO BLACKJACK!')
    print('=' * 35)
    main()
