#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int viralAdvertising(int n) {
    // Complete this function
    int likes = 2, total_likes = 2;
    for(int i = 1; i < n; i++){
        likes = ( likes * 3) / 2;
        total_likes += likes;
    }
    return total_likes;
}

int main() {
    int n; 
    scanf("%i", &n);
    int result = viralAdvertising(n);
    printf("%d\n", result);
    return 0;
}
