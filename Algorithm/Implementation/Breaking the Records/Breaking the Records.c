#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int* breakingRecords(int score_size, int* score, int *result_size) {
    // Complete this function
    *result_size = 2;
    static int result[2] = {0, 0};
    int min = score[0];
    int max = score[0];
    for(int i = i; i < score_size; i++){
        if(min > score[i]){
            min = score[i];
            result[1]++;
        }
        if(max < score[i]){
            max = score[i];
            result[0]++;
        }
    }
    return result;
}

int main() {
    int n; 
    scanf("%i", &n);
    int *score = malloc(sizeof(int) * n);
    for (int score_i = 0; score_i < n; score_i++) {
       scanf("%i",&score[score_i]);
    }
    int result_size;
    int* result = breakingRecords(n, score, &result_size);
    for(int result_i = 0; result_i < result_size; result_i++) {
        if(result_i) {
            printf(" ");
        }
        printf("%d", result[result_i]);
    }
    puts("");


    return 0;
}
