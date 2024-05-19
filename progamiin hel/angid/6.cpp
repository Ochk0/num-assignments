#include<iostream>
#include<cmath>
using namespace std;
int main(){
    float a,b,c,d;
    cin>>a>>b>>c>>d;
    float x = sqrt(pow(a+b, 2) + d)/c;
    cout<<x;
}