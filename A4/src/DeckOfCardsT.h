#ifndef DECKOFCARDST_H
#define DECKOFCARDST_H

#include "CardT.h"
#include <string>


using namespace std;


class DeckOfCardsT {

	private:
	//variable card with a pointer to deck
		CardT deck[Size]; 
	//keep track of what card you are dealing with
		int currentCard;
	

	public:
	// Default constructor: assigns the 52 cards to deck
		DeckOfCardsT();
	//It finds the color of the card	
		string color(CardT a);
	//shuffles the deck once all the cards are assigned
		void shuffle();
	//deals out one card from the deck of 52, refrences class card
		CardT dealCard();
	
		
};

#endif
