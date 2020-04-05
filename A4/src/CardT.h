#ifndef CARDT_H
#define CARDT_H

#include <string>
#define Size 52

using namespace std;


//create a class called card
class CardT{
	private:
//create two card variables face and suit
		string face;
		string suit;
		
	public:
//default constructer
		CardT();
//constructer with parameters
		CardT(string cardFace, string cardSuit);
//return the face of the card
		string Face();
//return the suit of the card		
		string Suit();

};

#endif
