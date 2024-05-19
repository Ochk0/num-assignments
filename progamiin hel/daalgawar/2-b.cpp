#include<iostream>
#include<cmath>
using namespace std;
int main(){
    float a,b,t;
    cin>>a>>b>>t;
    float c = sqrt(b*b+a*a-2*a*b*cos(t));
    cout<<c;
}