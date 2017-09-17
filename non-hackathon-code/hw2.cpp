//
//  hw2.cpp
//  
//
//  Created by Bryce Jacobson on 9/13/17.
//
//

#include "hw2.hpp"
#include <iostream>
#include <cmath> // math functions
#include <math.h> //gives pi

using namespace std;


double indvTemp(double xi, double yi, double L, double H){
    double computation = 0;
    
    double part1 = sin(((3.14)*xi)/L);
    double part2 = sinh(((3.14)*yi)/L);
    double part3 = sinh(((3.14)*H)/L);
    computation = 100 + (100*part1*part2)/part3;
    
    return computation;
    
}
int main(){
    double xyarray [1000][1000] = {0};

    double L = 3;
    double H = 3;
    double xi = 0;
    double yi = 0;
    double sum = 0;
    for(int x=0;x<1000;x++){
        xi += L/1000;
        yi = 0;
        for (int y=0; y<1000; y++) {
            double number = indvTemp(xi,yi,3,3);
            xyarray[x][y] = number;
            sum += number;
            yi += H/1000;
        }
    }
    sum = sum/1000000;
    cout << sum << endl;
    
    
    
    return 0;
}
