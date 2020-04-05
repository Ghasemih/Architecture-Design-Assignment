#include "CardT.h"
#include <iostream>


using namespace std;

CardT::CardT() { }

//constructor with two parameters
CardT::CardT(string cardFace, string cardSuit)
{
//assigns the paraments above to the two variables face and suit
	this->face = cardFace;
	this->suit = cardSuit;
	
}

//print function defintion

string CardT::Face(){
//return the way the card will be displayed
	return (this->face);
}

string CardT::Suit(){
//return the way the card will be displayed
	return (this->suit);
}


