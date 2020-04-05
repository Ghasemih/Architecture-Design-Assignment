#include <iostream>
#include <string>
#include "Exceptions.h"
#include "LineADT.h"

using namespace std;
int main(){
	
   PointT s(5,6);
   LineT lol(s, N, 5);
   cout << lol.strt().x() << endl;
   cout << lol.strt().y() << endl;
   cout << lol.orient() << endl;
   cout << lol.len() << endl;

   cout << lol.end().x() << endl;
   cout << lol.end().y() << endl;

   cout << lol.flip().orient() << endl;

   cout << lol.rotate(CCW).orient() << endl;

   cout << lol.translate(1,1).strt().x() << endl;
   cout << lol.translate(1,1).strt().y() << endl;


   return 0;
 }		

