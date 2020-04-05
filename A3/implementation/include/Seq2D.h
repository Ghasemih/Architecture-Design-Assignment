/**
 *  \file PathADT.h
 *  \brief A documented file
 */

#include <iostream>
#include "PathADT.h"
#include "MapTypes.h"
#include "Exceptions.h"

#ifndef SEQ2D_H
#define SEQ2D_H

/**
 *  \brief Class representing a sequence of sequence of T
 *  \details Coordinates are Vector, double, unsigned integers.
 */
template <class T>
class Seq2D(T){
	private:
		/// Sequence of sequence of T
		vector<vector<T>> s;
		
		/// scale is integer
		double scale;
		
		/// nRow is integer
		unsigned int nRow;
		
		/// nCol is integer
		unsigned int nCol;
		
		/**
    	*  \brief Gets a path and find points on it
     	*  \param p is a path
     	*  \return sets of points
     	*/
		vector<PointT> pointsInPath(PathT p);
		
		/**
    	*  \brief Gets a  and find points on it
     	*  \param p is a path
     	*  \return sets of points
     	*/
		vector<PointT> pointsInLine(LineT l);
			
	public:
		
		/**
    	*  \brief construct a vectors of T 
     	*  \param S 
     	*  \param scl is scale
       	*/
		Seq2D(vector<vector<T>> S, double scl);
		
		/**
    	*  \brief sets point to type t  
     	*  \param p is a point
     	*  \param v 
       	*/
		void set(PointT p , T v);
		
		/**
    	*  \brief gets the point p  
     	*  \param p is a point
     	*  \return it returns point
       	*/	
		T get(PointT p);
		
		/**
    	*  \brief get value of the row
     	*  \return a value for row
       	*/
		unsigned int getNumRow();
	
		/**
    	*  \brief get value of the col
     	*  \return a value for col
       	*/
		unsigned int getNumCol();
		
		/**
    	*  \brief it returns scale value
     	*  \return scale
       	*/	
		double getScale();
		
		/**
    	*  \brief it counts how many times t would be in the s sequence
     	*  \param t 
     	*  \return counts the number
       	*/	
		int count(T t);
		
		/**
    	*  \brief it counts how many times t would be in line l(breaks the line l to points and then checks it)
     	*  \param t 
     	*  \param l 
     	*  \return counts the number
       	*/
		int count(LineT l, T t);
		
		/**
    	*  \brief it counts how many times t would be in path pthx(breaks the pth to points and then checks it)
     	*  \param t 
     	*  \param pth 
     	*  \return counts the number
       	*/	
		int count(PathT pth, T t);
		
		/**
    	*  \brief finding the length of path by using pth
     	*  \param pth 
     	*  \return length in double
       	*/	
		double length(PathT pth);
		
		/**
    	*  \brief using point p1 and p2 to check if there is path between those two points
     	*  \param p2 a point
     	*  \param p1 a point
     	*  \return boolean based on if there is path between p1 and p2
       	*/	
		bool connected(PointT p1, PointT p2);
			
};

#endif
