#include<iostream>
#include<cmath>
using namespace std;
int main(){
    float a,b,c,d;
    cin>>a>>b>>c>>d;
    float top = sqrt( pow(pow(a,3) + b/c, 2) + d );
    float bottom = pow(d,2) - a*b/c;
    cout<< top/bottom*d;
}