#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int migratoryBirds(int ar_size, int* ar) {
    // Complete this function
    int type_bird,max = 0; 
    for(int i = 1; i <= 5; i++){
        int count = 0;
        for(int j = 0; j < ar_size; j++){
            if(i == ar[j])
                count++;
        }
        if(count > max){
            max = count;
            type_bird = i;
        }
    }
    return type_bird;
}

int main() {
    int n; 
    scanf("%i", &n);
    int *ar = malloc(sizeof(int) * n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       scanf("%i",&ar[ar_i]);
    }
    int result = migratoryBirds(n, ar);
    printf("%d\n", result);
    return 0;
}
