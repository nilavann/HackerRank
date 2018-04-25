#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int arr[6][6], max;
    for(int arr_i = 0; arr_i < 6; arr_i++){
       for(int arr_j = 0; arr_j < 6; arr_j++){
          
          scanf("%d",&arr[arr_i][arr_j]);
       }
    }
    int flag = 0;
    for(int arr_i = 0; arr_i < 4; arr_i++){
       for(int arr_j = 0; arr_j < 4; arr_j++){
          int sum = 0;
          for(int i = arr_i; i < arr_i + 3; i++){
              for( int j = arr_j; j < arr_j + 3; j++){
                  if( (i == arr_i + 1 && j == arr_j) || (i == arr_i + 1 && j == arr_j + 2)){
                      //printf("  ");
                      continue;
                  }
                  else{
                      //printf("%d ",arr[i][j]);
                      sum += arr[i][j];
                  }
              }
              //printf("\n");
          }
           if(flag == 0){
               max = sum;
               flag = 1;
           }
          if(sum > max)
              max = sum;
       }
    }
    printf("%d", max);
    return 0;
}
