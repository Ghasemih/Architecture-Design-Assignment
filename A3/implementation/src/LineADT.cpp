#include <iostream>
#include <string>
#include "Exceptions.h"
#include "LineADT.h"


using namespace std;


LineT::LineT(PointT st, CompassT ornt, unsigned int l){

	if (l = 0){
		throw invalid_argument;
}

	this->s = st;
	this->o = ornt;
	this->L = l;
}
		
PointT LineT:: strt(){	
	return PointT(s.x(),s.y());
}
		
PointT LineT::end(){
	if ( this->o == W){		
		return PointT((s.x()-(this->L-1)), s.y());
}
	if (this->o == E){
		return PointT((s.x()+(this->L-1)), s.y());
	}
	if (this->o  == N){
		return PointT(s.x(), (s.y()+(this->L-1)));
	}
	if (this->o  == S) {
		return  PointT(s.x(), (s.y()-(this->L-1)));
	}
}
		
CompassT LineT:: orient(){
	return this->o;
}
		
int LineT::len(){
	return this->L;
}
		
LineT LineT::flip(){
	if ( this->o  == W){
		return LineT(s, E, L);
	}
	if (this->o  == E){
		return LineT(s, W, L);
	}
	if (this->o  == N){
		return  LineT(s, S, L);
	}
	if (this->o  == S){
				
		return  LineT(s, N, L);
	}
}
		
LineT LineT::rotate(RotateT r){
	if (r == CW){
		if ( this->o  == N){
			return LineT(s, E, L);
	}
		if (this->o  == S){
			return LineT(s, W, L);
		}
		if (this->o  == W){
			return  LineT(s, N, L);
		}
		if (this->o  == E){
				
			return  LineT(s, S, L);
		}
}
			
	else {
		if (this->o == N){
			return LineT(s, W, L);
		}
		if (this->o  == S){
			return LineT(s, E, L);
		}
		if (this->o  == W){
			return  LineT(s, S, L);
		}
		if (this->o  == E) {
				
			return  LineT(s, N, L);
		}
	}
}
		
LineT LineT::translate(int Delta_x, int Delta_y){
	return LineT(s.translate(Delta_x, Delta_y), this->o, this->L);
}	

	

