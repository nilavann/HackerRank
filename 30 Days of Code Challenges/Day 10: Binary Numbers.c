#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n; 
    scanf("%d",&n);
    int max = 0,count = 0;
    while( n > 0){
        if( n % 2 == 1)
            count++;
        else{
            if( count > max)
                max = count;
                count = 0;
        }
        n /= 2;
    }
    if( count > max)
        max = count;
    printf( "%d", max);
    return 0;
}
