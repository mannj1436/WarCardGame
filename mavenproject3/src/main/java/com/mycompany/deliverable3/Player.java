package com.mycompany.deliverable3;

import java.util.List;
import java.util.ArrayList;

public class Player {
    private List<Card> hand;

    public Player() {
        hand = new ArrayList<>();
    }

    public void addCardToHand(Card card) {
        hand.add(card);
    }

    public int finalScore() {
        int score = 0;
        for (Card card : hand) {
            score += card.getValue();
        }
        return score;
    }

    public List<Card> getHand() {
        return hand;
    }

    @Override
    public String toString() {
        return "Player's hand: " + hand;
    }
}
