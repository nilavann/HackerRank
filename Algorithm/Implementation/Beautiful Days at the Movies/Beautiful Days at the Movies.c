#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int reversenumber(int n){
    int reversed = 0;
    while( n > 0){
        reversed *= 10;
        reversed += n % 10;
        n = n / 10;
    }
    return reversed;
}
int beautifulDays(int i, int j, int k) {
    // Complete this function
    int count = 0;
    for( ; i <= j; i++){
        int reversednumber = reversenumber(i);
        if( ( i - reversednumber) % k == 0)
            count++;
    }
    return count;
}

int main() {
    int i; 
    int j; 
    int k; 
    scanf("%i %i %i", &i, &j, &k);
    int result = beautifulDays(i, j, k);
    printf("%d\n", result);
    return 0;
}
