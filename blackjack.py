import random

dealer_hand = []
player_hand = []
player_score = 0
dealer_score = 0
hit_counter = 0
reward = 0
bust = False

# Optimized function: just passes the hand list and returns the smart sum
def calculate_hand(hand):
    score = sum(hand)
    if 11 in hand and score > 21:
        score = score - 10
    return score

# Limit setter
bet_limits = {'Golden Casino': 1000, 'Silver Casino': 750, 'Bronze Casino': 500}
limit_decider = random.randint(1, 3)

if limit_decider == 1:
    casino = 'Golden Casino'
    bet_limit = bet_limits['Golden Casino']
elif limit_decider == 2:
    casino = 'Silver Casino'
    bet_limit = bet_limits['Silver Casino']
else:
    casino = 'Bronze Casino'
    bet_limit = bet_limits['Bronze Casino']

# Added the missing 'f' here so {casino} prints correctly
print(f"Welcome to {casino}'s Blackjack simulator!")
start = input('Shall we begin? (Type Y to start, or HELP for rules): ')

# Bet validation
while 'Y' in start.upper():
    try:
        bet = float(input('How much are you willing to bet? '))
    except ValueError:
        print("Invalid input! Please type numbers only!")
        continue
    except Exception:
        print("Something went wrong! Please try again")
        continue

    if bet > bet_limit:
        print(f"Sorry! According to {casino}'s policy, the bet limit has been set to ${bet_limit}. Please try again. ")
        continue
    break

# --- GAMEPLAY LOGIC (Fixed Indentation) ---
if 'Y' in start.upper():
    print("\nGreat! Let's begin!")
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    # Initial Deals (Starting at 0 index to include all cards)
    player_hand.append(cards[random.randint(0, 13)])
    player_hand.append(cards[random.randint(0, 13)])
    player_score = calculate_hand(player_hand)
    print(f"Your hand is {player_hand}. Your hand sum is {player_score}")

    dealer_hand.append(cards[random.randint(0, 13)])
    dealer_hand.append(cards[random.randint(0, 13)])
    print(f"The dealer has a face-up card of {dealer_hand[0]}.")

    # Player's Turn Loop
    while player_score < 21:
        action = input('What would you like to do? (Hit/Stand): ')
        if "HIT" in action.upper():
            hit_counter += 1
            player_hand.append(cards[random.randint(0, 13)])
            player_score = calculate_hand(player_hand)
            print(f"Your hand is {player_hand}. Your hand sum is {player_score}")
        elif "STAND" in action.upper():
            print(f"You have decided to stand with a sum of {player_score}.")
            break
        else:
            print("Invalid input! You can either hit or stand.")
            continue

    # Dealer's Turn
    dealer_score = calculate_hand(dealer_hand)
    if player_score <= 21:
        print(f'\nThe dealer reveals their face-down card. Their total sum is {dealer_score}')

        # Dealer automatically plays correctly to 17
        while dealer_score < 17:
            dealer_hand.append(cards[random.randint(0, 13)])
            dealer_score = calculate_hand(dealer_hand)
            print(f"The dealer has chosen to hit. Dealt: {dealer_hand[-1]}. Their sum is now {dealer_score}.")

    # Final score and result checks
    print("\n--- FINAL RESULT ---")
    if player_score > 21:
        print(f"You busted! You lost! You lose ${bet:.2f}.")
    elif dealer_score > 21:
        print(f"The dealer busted! You won! You win ${bet * 2:.2f}!")
    elif player_score > dealer_score:
        if hit_counter == 0 and player_score == 21:
            print(f"It's your lucky day! Natural Blackjack on turn one! You win ${bet + (bet * 1.5):.2f}!")
        else:
            print(f"You won! Your {player_score} beats the dealer's {dealer_score}. You win ${bet * 2:.2f}!")
    elif dealer_score > player_score:
        print(f"You lost! The dealer's {dealer_score} beats your {player_score}. You lose ${bet:.2f}.")
    else:
        print(f"You tie! Both hit {player_score}. You got your money back.")

# --- HELP / QUIT MENU ---
else:
    if "HELP" in start.upper():
        print('''\nThe goal of Blackjack is to beat the dealer’s hand total without exceeding 21.

Both you and the dealer start with two cards; only one of the dealer's cards is face-up.
Cards 2–10 are face value, face cards (J, Q, K) are worth 10, and Aces can equal 1 or 11.

On your turn, choose to Hit (take a card) or Stand (keep your total).
If you exceed 21, you Bust and lose automatically.
Otherwise, the dealer reveals their card and must hit until they reach at least 17. Highest hand under 22 wins!''')
    elif "N" in start.upper():
        print("Goodbye.")
    else:
        print("Invalid input.")
