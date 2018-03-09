#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int* solve(int grades_size, int* grades, int *result_size){
    // Complete this function
    *result_size = grades_size;
    for(int i = 0; i < grades_size; i++){
        int max;
        if(grades[i] < 38)
            continue;
        else{
            if(grades[i] % 10 > 5)
                max = (grades[i] / 10 + 1) * 10;
            else
                max = ((grades[i] /10) * 10) + 5;
            if((max - grades[i]) < 3)
                    grades[i] = max;
        }
    }
    return grades;
}

int main() {
    int n; 
    scanf("%d", &n);
    int *grades = malloc(sizeof(int) * n);
    for(int grades_i = 0; grades_i < n; grades_i++){
       scanf("%d",&grades[grades_i]);
    }
    int result_size;
    int* result = solve(n, grades, &result_size);
    for(int result_i = 0; result_i < result_size; result_i++) {
        if(result_i) {
            printf("\n");
        }
        printf("%d", result[result_i]);
    }
    puts("");
    

    return 0;
}
