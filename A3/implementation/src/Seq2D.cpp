#include <iostream>
#include "Seq2D.h"
#include "Exceptions.h"


using namespace std;

template <class T>
Seq2D<T>::Seq2D(vector<vector<T>> S, double scl){
	if ((scl <= 0) || (S.size()==0) || (S[0].size()==0) ){
		throw invalid_argument();
}
	for (int i=0 ; i < S.size; i++){
		if (S[i].size() != S[0].size()){
			throw invalid_argument();
		}
	}
		
	this->s = S;
	this->scale = scl;
	this->nRow = S[0].size();
	this->nCol = S.size();
}

template <class T>
void Seq2D<T>::set(PointT p , T v){
	if (!validPoint(p)){
		throw outside_bounds();
	}

	this->s[p.y()][p.x()] = v;
}

template <class T>
T Seq2D<T>::get(PointT p){
	if (!validPoint(p)){
		throw outside_bounds();
	}

	return this->s[p.y()][p.x()];
}


template <class T>
unsigned int Seq2D<T>::getNumRow(){
	return this-> nRow;
}

template <class T>
unsigned int Seq2D<T>::getNumCol(){
	return this-> nCol;
}

template <class T>
double Seq2D<T>::getScale(){
	return this-> scale;
}

template <class T>
int Seq2D<T>::count(T t){
	int d =0;
	for (int i =0; i < getNumRow() ; i++){
		for (int j = 0; j < getNumCol() ; j++){
			if (this->s[i][j] == t && validRow(i) && validCol(j)){
				d += 1;
			}
		}
	}
	return d;
}

template <class T>
int Seq2D<T>::count(LineT l, T t){
	int d =0;
	vector <PointT> p;
	if (!validLine(l)){
		throw invalid_argument();
	}

	p = pointsInLine(l);
	for (int i=0 ; i< p.size(); i++){
		if (this->s[p[i].y()][p[i].x()] == t){
			d +=1;
		}
	}
	
	return d;
}

template <class T>
int Seq2D<T>::count(PathT pth, T t){
	int d=0;
	vector <PointT> p;
	
	if (!validPath(pth)){
		throw invalid_argument();
	}
	
	p = pointsInPath(pth);
	for (int i=0 ; i< p.size(); i++){
		if (this->s[p[i].y()][p[i].x()] == t){
			d +=1;
		}
	}	

	return d;
}

template <class T>
double Seq2D<T>::length(PathT pth){
	if (!validPath(pth)){
		throw invalid_argument();
	}
	
	double d;
	d = pth.len() * getScale();
	return d;
}


template <class T>
bool Seq2D<T>::connected(PointT p1, PointT p2){
	if (!validPoint(p1) || !validPoint(p2)){
		throw invalid_argument;
	}

	

}

template <class T>
bool Seq2D<T>::validRow(int i){
	if (0=< i < getNumRow())
		return true;
}

template <class T>
bool Seq2D<T>::validCol(int j){
	if (0=< j < getNumCol())
		return true;
}

template <class T>
bool Seq2D<T>::validPoint(PointT p){
	if (validRow (p.y()) && validCol(p.x()))
		return true;
}

template <class T>
bool Seq2D<T>::validLine(LineT l){
	p = pointsInLine(l);
	for (int i= 0; i< s.size(); i++){
		if (validPoint(p[i]) == false){
			return false;
		}
	return true;
	}
}

template <class T>
bool Seq2D<T>::validPath(PathT pth){
	p = pointsInPath(pth);
	if (validPoint(p[i]) == false){
		return false;
	}
	return true;
}

template <class T>
vector<PointT> Seq2D<T>::pointsInLine(LineT l){
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

template <class T>
vector<PointT> Seq2D<T>::pointsInPath(PathT p){
	vector<PointT> d;
	for (int i = 0; i < p.len(); i++){
		vector<PointT> a = 	pointsInLine(p.line(i));
		d.insert(d.end(), a.begin(), a.end());
	}
}

template class Seq2D<LanduseT>;
template class Seq2D<int>;
