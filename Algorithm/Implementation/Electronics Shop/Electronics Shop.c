#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int getMoneySpent(int* keyboards, int* drives, int s, int n, int m){
    // Complete this function
    int i,j;
    for(i = 0; i< n - 1; i++){
        int big_index = i;
        for(j = i + 1; j < n; j++){
            if(keyboards[big_index] < keyboards[j])
                big_index = j;
        }
        int temp = keyboards[i];
        keyboards[i] = keyboards[big_index];
        keyboards[big_index] = temp;
    }
    for(i = 0; i< m - 1; i++){
        int small_index = i;
        for(j = i + 1; j < m; j++){
            if(drives[small_index] > drives[j])
                small_index = j;
        }
        int temp = drives[i];
        drives[i] = drives[small_index];
        drives[small_index] = temp;
    }
    int result = -1;
    for(i = 0,j = 0; i < n; i++){ 
        for(; j < m; j++){
            if( keyboards[i] + drives[j] > s)
                break;
            if( keyboards[i] + drives[j] > result)
                result = keyboards[i] + drives[j];
        }
    }
    return result;
}

int main() {
    int s; 
    int n; 
    int m; 
    scanf("%d %d %d", &s, &n, &m);
    int *keyboards = malloc(sizeof(int) * n);
    for(int keyboards_i = 0; keyboards_i < n; keyboards_i++){
       scanf("%d",&keyboards[keyboards_i]);
    }
    int *drives = malloc(sizeof(int) * m);
    for(int drives_i = 0; drives_i < m; drives_i++){
       scanf("%d",&drives[drives_i]);
    }
    //  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    int moneySpent = getMoneySpent(keyboards, drives, s, n, m);
    printf("%d\n", moneySpent);
    return 0;
}
