package com.mycompany.deliverable3;

public class Main {
    public static void main(String[] args) {
        Game game = new Game();
        game.startGame();

        for (int i = 0; i < 5; i++) {
            game.playRound();
            game.displayPlayerHand();
            System.out.println("Score after round " + (i + 1) + ": " + game.roundResult());
            System.out.println("Remaining cards in deck: " + game.remainingCardsInDeck());
            System.out.println("--------------------------------------------------");
        }

        System.out.println("Final Score: " + game.finalResult());
    }
}
