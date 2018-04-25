#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

char* isprime(int number){
    if( number == 1)
        return "Not prime";
    else{
        int n = sqrt(number) + 1;
        for(int j = 2;j < n; j++){
            if( number % j == 0)
                return "Not prime";
        }
    }
    return "Prime";
}
int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int n;
    scanf("%d",&n);
    for( int i = 0; i < n ; i++){
        int number,f=0;
        scanf("%d",&number);
        printf("%s\n",isprime(number));
    }
    return 0;
}
