/**
 *  \file LineADT.h
 *  \brief A documented file
 */

#include "PointADT.h"
#include "MapTypes.h"

#ifndef LINET_H
#define LINET_H

/**
 *  \brief Class representing a line in the 2D plane
 *  \details Coordinates are, unsigned integer, PointT, and CompassT.
 */
class LineT{
	private:
		/// Length of the Line
		unsigned int L;
		/// Starting point on the line
		PointT s;
		/// Direction of the line
		CompassT o;
		
	public:
		/**
    	*  \brief Constructs a new line
     	*  \param st is starting point on the lin
     	*  \param ornt is direction of the line
     	*  \param l is lenght of the line
     	*/
		LineT(PointT st, CompassT ornt, unsigned int l);
		
		/**
     	*  \brief gets the st
     	*  \return startign point(s)
     	*/
		PointT strt();
		
		/**
     	*  \brief find the end point on the line
     	*  \return end point on the line by using st and l to find the end point
     	*/
		PointT end();
		
		/**
     	*  \brief gets direction of the line
     	*  \return direction of the line 
     	*/
		CompassT orient();
		
		/**
     	*  \brief finding the lenght of the line 
     	*  \return l lenght of the line 
     	*/
		int len();
		
		/**
     	*  \brief flip the direction of the line 
     	*  \return a line that its direction has been fliped 
     	*/
		LineT flip();
		
		/**
     	*  \brief it rotates 90 degree from its first location based on clockwise and counter clock
		*	wise. 
     	*  \param r is either clock wise or counter clock wise
     	*  \return a line has been rotated 
     	*/
		LineT rotate(RotateT r);
		
		/**
    	*  \brief translate line to a new line 
     	*  \param Delta_x adding to x to make a new x
     	*  \param Delta_y adding to y to make a new y
     	*/
		LineT translate(int Delta_x, int Delta_y);
			
};
#endif
