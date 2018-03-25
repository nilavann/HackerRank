#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int equalizeArray(int arr_size, int* arr) {
    // Complete this function
    int *unique = malloc(sizeof(int) * arr_size);
    int len = -1;
    int maxAccurance = 0;
    for(int i = 0; i < arr_size; i++){
        int count = 0, flag = 0;
        //check for duplicate
        for(int k =0 ;k <= len;k++){
            if(unique[k] == arr[i]){
                flag = 1;
                break;
            }
        }
        //if duplicate continue
        if(flag == 1)
            continue;
        //add to unique if it is not duplicate
        unique[++len] = arr[i];
        //counting num be of times arr[i] present in arr
        for(int j = 0; j< arr_size; j++){
            if(arr[i] == arr[j])
                count++;
        }
        if(count > maxAccurance)
            maxAccurance = count;
    }
    return arr_size - maxAccurance;
}

int main() {
    int n; 
    scanf("%i", &n);
    int *arr = malloc(sizeof(int) * n);
    for (int arr_i = 0; arr_i < n; arr_i++) {
       scanf("%i",&arr[arr_i]);
    }
    int result = equalizeArray(n, arr);
    printf("%d\n", result);
    return 0;
}
