#include<iostream>
#include<cmath>
using namespace std;
int main() {
    float a,b,c;
    cin>>a>>b>>c;
    float z = sqrt(b*b-4*a*c);
    float x1 = (-b + z)/(2*a);
    float x2 = (-b - z)/(2*a);
    cout<<x1<<" "<< x2;
}