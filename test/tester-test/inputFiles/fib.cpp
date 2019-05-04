#include <iostream>
using namespace std;

int fibs(int n){
     if(n == 0 || n==1){
          return 1;
     }
     else{
          return fibs(n-1)+fibs(n-2);
     }
}

int main(){
     int n;
     cin>>n;
     int out = fibs(n);
     cout<<out<<endl;
}