#include <iostream>
#include <cstdlib>
#include "PointADT.h"

using namespace std;

PointT::PointT() { }

PointT:: PointT(int x,int y){
	this->xc = x;
	this->yc = y;
}
		
int PointT::x(){
	return this->xc;
}

int PointT::y(){
	return this->yc;
}

PointT PointT::translate(int Delta_x, int Delta_y){
	return PointT( Delta_x+x(), Delta_y+y() );
}


/*int main()
{
    // Constructor called
    PointT p1(10, 15); 
 
    // Access values assigned by constructor
    cout << "p1.x = " << p1.x() << ", p1.y = " << p1.y() <<endl;
    
    
 	p1.translate(10, 15); 
    // Access values assigned by constructor
    cout << "p1.x = " << p1.x() << ", p1.y = " << p1.y();
 
    return 0;
}*/
