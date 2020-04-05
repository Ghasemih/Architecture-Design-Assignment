#include <iostream>
#include <cstdlib>
#include <ctime>

#include "DeckOfCardsT.h"


DeckOfCardsT::DeckOfCardsT(){
	
	string faces[] = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};
	string suits[] = {"Hearts", "Diamonds", "Clubs", "Spades"};	 

	
	deck = new CardT[Size];
	currentCard = 0;
	
	for(int count = 0; count < Size; count++){
		this->deck[count] = CardT(faces[count % 13], suits[count / 13]);
	}
}

string DeckOfCardsT::color(CardT a){
//it returns the color of the card
	if (a.Suit() =="Spade" || a.Suit() =="Club"){
		return "Black";
}
	else{
		return "Red";
	}
	
}



void DeckOfCardsT::shuffle(){

	for(int first = 0; first < Size; first++){

		int second = (rand() + time(0)) % Size;
		CardT temp = this->deck[first];
		this->deck[first] = this->deck[second];
		this->deck[second] = temp;
	}	
}

CardT DeckOfCardsT::dealCard(){
	
	if(this->currentCard > Size){
		shuffle();
	}
	
	if( this->currentCard < Size)	{
		return (this->deck[this->currentCard++]);
	}
	
	return (this->deck[0]);
}













