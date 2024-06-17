import random

# Define the ranks and suits
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

# Create the deck
deck = [(rank, suit) for rank in ranks for suit in suits]
random.shuffle(deck)

# Split the deck between two players
half_deck = len(deck) // 2
player1_deck = deck[:half_deck]
player2_deck = deck[half_deck:]

def card_value(card):
    rank, suit = card
    return ranks.index(rank)

def play_war(player1_deck, player2_deck):
    round_counter = 0
    while player1_deck and player2_deck:
        round_counter += 1
        print(f"Round {round_counter}:")
        player1_card = player1_deck.pop(0)
        player2_card = player2_deck.pop(0)
        
        print(f"Player 1 plays {player1_card[0]} of {player1_card[1]}")
        print(f"Player 2 plays {player2_card[0]} of {player2_card[1]}")

        if card_value(player1_card) > card_value(player2_card):
            print("Player 1 wins the round")
            player1_deck.extend([player1_card, player2_card])
        elif card_value(player1_card) < card_value(player2_card):
            print("Player 2 wins the round")
            player2_deck.extend([player1_card, player2_card])
        else:
            print("War!")
            war_cards = [player1_card, player2_card]
            while True:
                if len(player1_deck) < 4:
                    print("Player 1 cannot continue war. Player 2 wins the game!")
                    player2_deck.extend(player1_deck + war_cards)
                    player1_deck.clear()
                    break
                if len(player2_deck) < 4:
                    print("Player 2 cannot continue war. Player 1 wins the game!")
                    player1_deck.extend(player2_deck + war_cards)
                    player2_deck.clear()
                    break
                
                war_cards.extend([player1_deck.pop(0) for _ in range(4)])
                war_cards.extend([player2_deck.pop(0) for _ in range(4)])
                
                print("War cards added. Players reveal their war cards...")
                player1_war_card = war_cards[-4]
                player2_war_card = war_cards[-1]

                print(f"Player 1 reveals {player1_war_card[0]} of {player1_war_card[1]}")
                print(f"Player 2 reveals {player2_war_card[0]} of {player2_war_card[1]}")
                
                if card_value(player1_war_card) > card_value(player2_war_card):
                    print("Player 1 wins the war")
                    player1_deck.extend(war_cards)
                    break
                elif card_value(player1_war_card) < card_value(player2_war_card):
                    print("Player 2 wins the war")
                    player2_deck.extend(war_cards)
                    break
                else:
                    print("Another war!")

    if player1_deck:
        print("Player 1 wins the game!")
    else:
        print("Player 2 wins the game!")

# Play the game
play_war(player1_deck, player2_deck)