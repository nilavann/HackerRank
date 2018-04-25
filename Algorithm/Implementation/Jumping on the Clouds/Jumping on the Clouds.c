#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int jumpingOnClouds(int c_size, int* c) {
    // Complete this function
    int jumps = 0, clouds = -1;
    for( int i = 0; i < c_size; i++){
        // non thuder clods increment
        if( c[i] == 0)
            clouds++;
        // thuder clouds (+ 1) since we jump thuder cloud other find min jumps
        else{
            jumps += clouds / 2;
            jumps += ( clouds % 2 ) + 1;
            clouds = -1;
        } 
    }
    jumps +=  clouds / 2;
    jumps +=  clouds % 2;
    return jumps; 
}

int main() {
    int n; 
    scanf("%i", &n);
    int *c = malloc(sizeof(int) * n);
    for (int c_i = 0; c_i < n; c_i++) {
       scanf("%i",&c[c_i]);
    }
    int result = jumpingOnClouds(n, c);
    printf("%d\n", result);
    return 0;
}
