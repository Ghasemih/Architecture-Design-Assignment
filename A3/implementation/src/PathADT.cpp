#include <iostream>
#include "PathADT.h"
#include <vector>
#include "Exceptions.h"

using namespace std;

PathT:: PathT() { }

PathT:: PathT(PointT st, CompassT ornt, unsigned int l){
	this->s.push_back(LineT(st,ornt,l));
}
		
PathT PathT::append(CompassT ornt, int l){
	this->s.push_back(LineT(adjPt(ornt), ornt, l));
}
		
PointT PathT::strt(){
	return this->s[0].strt();
	}
		
PointT PathT::end(){
	return this->s[size()-1].end();
}
		
LineT PathT::line(int i){
	if (this->s.size()<=i) {
		throw outside_bounds;
	}

	return this->s[i];
}
		
int PathT::size(){
	return this->s.size();
}
		
int PathT::len(){
	int d = 0;
	for (int i=0; i< this->s.size(); i++){
		d = d + this->s[i].len();	
	}
	return d;
}
		
PathT PathT::translate(int x, int y){
	PathT d;
	for (int i =0 ; i < this->s.size(); i++){
		d.s.push_back(this->s[i].translate(x, y));
	}
	return d;
}

vector<PointT> pointsInLine(LineT l){
	vector <PointT> a;
	for (int i= 0; i< l.len(); i++){
		if(l.orient()== N){
			a.push_back(l.strt().translate(0, i));
		}
		if(l.orient()== S){
			a.push_back(l.strt().translate(0, -i));
		}
		if(l.orient()== E){
			a.push_back(l.strt().translate(i, 0));
		}
		if(l.orient()== W){
			a.push_back(l.strt().translate(-i, 0));
		}
	}
	return a;
	
}

PointT PathT::adjPt(CompassT ornt){
	if ( ornt == N){		
		return this->s[this->s.size()-1].end().translate(0,1);
	}
	if ( ornt == S){
		return this->s[this->s.size()-1].end().translate(0,-1);
	}
	if ( ornt == W){
		return  this->s.[this->s.size()-1].end().translate(-1,0);
	}
	if ( ornt == E) {
				
		return  this->s[this->s.size()-1].end().translate(1,0);
	}
	
	return this->s[this->s.size()-1].end().translate(0,0);
}




