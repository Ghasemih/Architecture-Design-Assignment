#include <iostream>
#include <cstdlib>
#include "PointADT.h"

using namespace std;
int main()
{
    // Constructor called
    PointT p1(10, 15); 
 
    // Access values assigned by constructor
    cout << "p1.x = " << p1.x() << ", p1.y = " << p1.y() <<endl;
    
    
 	p1.translate(10, 15); 
    // Access values assigned by constructor
    cout << "p1.x = " << p1.x() << ", p1.y = " << p1.y();
 
    return 0;
}
