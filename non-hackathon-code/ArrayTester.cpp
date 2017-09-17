//
//  ArrayTester.cpp
//  
//
//  Created by Bryce Jacobson on 9/12/17.
//
//

#include <iostream>

using namespace std;

int add(int x){
    return x;
}
int main(){
    int a [2][2] = {{0,0},{0,0}};
    
    a[0][0] = 1;
    a[0][1] = 2;
    a[1][0] = 3;
    a[1][1] = add(9);
    cout<< a[0][0]<< endl;
    cout<< a[0][1]<< endl;
    cout<< a[1][0]<< endl;
    cout<< a[1][1]<< endl;
    
    
    
    return 0;
}

