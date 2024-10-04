import cards
import random


def check_blackjack(cards):
    if sum(cards) == 21:
        return True
    return False

def determine_winner(user_cards, dealer_cards):
    print('=' * 35)
    #  If the user has a blackjack and the dealer doesn't, the user wins
    if sum(user_cards) == 21 and sum(dealer_cards) != 21:
        print('YOU GOT A BLACKJACK!, YOU WIN!')
        print(f'Your cards: {user_cards}')
        print(f'Dealer cards: {dealer_cards}')
        print(f'Your sum: {sum(user_cards)}')
        print(f'Dealer sum: {sum(dealer_cards)}')
    # If the dealer has a blackjack and the user doesn't, the dealer wins
    elif sum(dealer_cards) == 21 and sum(user_cards) != 21:
        print('YOU LOSE!')
        print('DEALER GOT A BLACKJACK!')
        print(f'Your cards: {user_cards}')
        print(f'Dealer cards: {dealer_cards}')
        print(f'Your sum: {sum(user_cards)}')
        print(f'Dealer sum: {sum(dealer_cards)}')
    elif sum(dealer_cards) > 21:
        print('DEALER WENT OVER 21. YOU WIN!')
        print(f'Your cards: {user_cards}')
        print(f'Dealer cards: {dealer_cards}')
        print(f'Your sum: {sum(user_cards)}')
        print(f'Dealer sum: {sum(dealer_cards)}')
    elif sum(user_cards) > 21:
        print('YOU WENT OVER 21. YOU LOSE!')
        print(f'Your cards: {user_cards}')
        print(f'Dealer cards: {dealer_cards}')
        print(f'Your sum: {sum(user_cards)}')
        print(f'Dealer sum: {sum(dealer_cards)}')
    else:
        # If the user sum is greater than the dealer sum, but the user sum is less than 21 the user wins
        if sum(user_cards) < 21 and sum(user_cards) > sum(dealer_cards):
            print('YOU WIN!')
            print(f'Your cards: {user_cards}')
            print(f'Dealer cards: {dealer_cards}')
            print(f'Your sum: {sum(user_cards)}')
            print(f'Dealer sum: {sum(dealer_cards)}')

        # If the dealer sum is greater than the user sum, but the dealer sum is less than 21 the dealer wins
        elif sum(dealer_cards) < 21 and sum(dealer_cards) > sum(user_cards):
            print('YOU LOSE!')
            print(f'Your cards: {user_cards}')
            print(f'Your sum: {sum(user_cards)}')
            print(f'Dealer cards: {dealer_cards}')
            print(f'Dealer sum: {sum(dealer_cards)}')
        else:
            print('IT\'S A DRAW!')
            print(f'Your cards: {user_cards}')
            print(f'Dealer cards: {dealer_cards}')
            print(f'Your sum: {sum(user_cards)}')
            print(f'Dealer sum: {sum(dealer_cards)}')

    print('=' * 35)

def play_again():
    play_again = input('Do you want to play again? (y/n): ')
    if play_again == 'y':
        main()
    exit()


def main():
    print('=' * 35)
    user_cards = []
    dealer_cards = []

    # Deal the initial cards for the user and dealer
    for x in range(2):
        user_cards.append(random.choice(cards.cards))
        dealer_cards.append(random.choice(cards.cards))

    print(f'Your cards: {user_cards}')
    print(f'Dealer cards: {dealer_cards[0]}, _')

    # Check for blackjack
    if check_blackjack(user_cards) and not check_blackjack(dealer_cards):
        print('You got a blackjack!')
        determine_winner(user_cards, dealer_cards)


    # Ask the user if they want to hit or stand
    while True:
        hit_or_stand = input('Do you want to hit or stand? (h/s): ')
        if hit_or_stand.lower() == 'h':
            user_cards.append(random.choice(cards.cards))
            print(f'Your cards: {user_cards}')
            print(f'Your sum: {sum(user_cards)}')
            if sum(user_cards) > 21 and 11 in user_cards:
                print('Converted 11 to 1')
                user_cards.remove(11)
                user_cards.append(1)
                print(f'Your cards: {user_cards}')
            elif sum(user_cards) == 21:
                determine_winner(user_cards, dealer_cards)
            elif sum(user_cards) > 21:
                print('You went over 21. You lose!')
                print(f'Dealer cards: {dealer_cards}')
                break
        else:
            break

    # Dealer's turn should only happen if the player hasn't busted
    if sum(user_cards) <= 21:
        # Dealer's turn
        while sum(dealer_cards) < 17:
            dealer_cards.append(random.choice(cards.cards))

    determine_winner(user_cards, dealer_cards)
    play_again()


if __name__ == '__main__':
    print('=' * 35)
    print('WELCOME TO BLACKJACK!')
    print('=' * 35)
    main()
