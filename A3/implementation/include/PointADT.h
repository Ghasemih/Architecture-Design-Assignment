/**
 *  \file PointADT.h
 *  \brief A documented file
 */

#include <iostream>
#ifndef POINTT_H
#define POINTT_H

/**
 *  \brief Class representing a point in the 2D plane
 *  \details Coordinates are integer values
 */
class PointT
{
	private:
		/// the x-coordinate
    	int xc;
    	/// the y-coordinate
    	int yc;
    
    public:
    	/**
     	*  \brief Constrructing point as 0
     	*  
     	*/
    	PointT();
    	
    	/**
    	*  \brief Constructs a new point
     	*  \param x The x-coordinate of the new point
     	*  \param y The y-coordinate of the new point
     	*/
    	PointT(int x, int y);
    	
    	/**
     	*  \brief Gets the x-coordinate of the point
     	*  \return The x-coordinate of the point
     	*/
    	int x();
    	
   		/**
    	*  \brief Gets the y-coordinate of the point
     	*  \return The y-coordinate of the point
     	*/
    	int y();
    	
    	/**
    	*  \brief translate a point to a new 
     	*  \param Delta_x adding to the previous x to make a new x
     	*  \param Delta_y adding to the previous y to make a new y
     	*/
    	PointT translate(int Delta_x, int Delta_y);   
};

#endif
