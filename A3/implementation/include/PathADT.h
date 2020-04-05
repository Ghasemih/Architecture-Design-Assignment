/**
 *  \file PathADT.h
 *  \brief A documented file
 */
 
#include <vector>
#include "LineADT.h"
#include "MapTypes.h" 
#include <iostream>

#ifndef PATHT_H
#define PATHT_H

using namespace std;

/**
 *  \brief Class representing a Path in the 2D plane. Having bunch of lines
 *  \details Coordinates are vector, PointTs.
 */
class PathT{
	private:
		/// Sequence of line
		vector <LineT> s;
		
		/**
    	*  \brief Constructs a new line
     	*  \param ornt is direction of the line
     	*  \return adjacent point
     	*/
		PointT adjPt(CompassT ornt);
		
		/**
    	*  \brief gets a line return points
     	*  \param l it is a line that points will be written from
     	*  \return points on the line of l
     	*/
		PointT pointsInLine(LineT l);
		
	public:
		/**
    	*  \brief constructing empty path
     	*/
		PathT();
		
		/**
    	*  \brief construct a path by using point length and direction
     	*  \param st is point 
     	*  \param ornt it is direction
     	*  \param l it is lenght of the line
       	*/
		PathT(PointT st, CompassT ornt, unsigned int l);
		
		/**
    	*  \brief appending line to the path
     	*  \param ornt it is direction
     	*  \param l it is lenght of the line
       	*/	
		PathT append(CompassT ornt, int l);
		
		/**
     	*  \brief gets the starting point of the line from sequence of s
     	*  \return startign point
     	*/
		PointT strt();
	
		/**
     	*  \brief gets the ending point of the line from sequence of s
     	*  \return ending point
     	*/	
		PointT end();
		
		/**
    	*  \brief gets a line from sequence of s by using index i
     	*  \param i is index in the sequence of s
     	*  \return a line by using index i
     	*/
		LineT line(int i);
		
		/**
    	*  \brief finding the size of the sequence
     	*  \return integer that displays how big is sequence s
     	*/	
		int size();
		
		/**
    	*  \brief adding length of each line from sequence s
     	*  \return a number 
     	*/		
		int len();
		
		/**
    	*  \brief translate all lines from sequence of s 
     	*  \param Delta_x adding to x to make a new x
     	*  \param Delta_y adding to y to make a new y
     	*/
		PathT translate(int Delta_x, int Delta_y);
		
};

#endif
