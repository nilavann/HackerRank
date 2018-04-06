#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int findDigits(int n) {
    // Complete this function
    int duplicate = n,count = 0;
    while( duplicate > 0){
        int diviser = duplicate % 10;
        if( diviser != 0 && ( n % diviser == 0))
            count++;
        duplicate /= 10;
    }
    return count;
}

int main() {
    int t; 
    scanf("%i", &t);
    for(int a0 = 0; a0 < t; a0++){
        int n; 
        scanf("%i", &n);
        int result = findDigits(n);
        printf("%d\n", result);
    }
    return 0;
}
