package com.mycompany.deliverable3;

public class Game {
    private Deck deck;
    private Player player;

    public Game() {
        deck = new Deck();
        player = new Player();
    }

    public void startGame() {
        deck.shuffle();
        System.out.println("Game started! Deck is shuffled.");
    }

    public void playRound() {
        Card drawnCard = deck.drawCard();
        if (drawnCard != null) {
            player.addCardToHand(drawnCard);
            System.out.println("Player drew: " + drawnCard);
        } else {
            System.out.println("No more cards to draw.");
        }
    }

    public void updateDeck() {
        // Update the deck, could be reshuffling or refilling the deck if required
        System.out.println("Deck updated.");
    }

    public int roundResult() {
        return player.finalScore();
    }

    public int finalResult() {
        return player.finalScore();
    }

    public void displayPlayerHand() {
        System.out.println(player);
    }

    public int remainingCardsInDeck() {
        return deck.remainingCards();
    }
}
