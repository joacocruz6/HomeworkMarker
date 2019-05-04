#include <stdio.h>
int fibs(int n){
     if(n == 0 || n == 1){
          return 1;
     }
     else{
          return fibs(n-1) + fibs(n-2);
     }
}
int main(){
     int in;
     scanf("%d",&in);
     int out = fibs(in);
     printf("%d\n",out);
     return 0;
}