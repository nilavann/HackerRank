#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n,k,anna_share,sum = 0;
    scanf("%d %d",&n,&k);
    int *arr = malloc(sizeof(int) * n);
    for(int i=0; i < n; i++){
        scanf("%d",&arr[i]);
    }
    scanf("%d",&anna_share);
    for(int i = 0; i < n; i++){
        if( i == k)
            continue;
        sum += arr[i];
    }
    int correct_share = sum/2;
    if(correct_share == anna_share)
        printf("Bon Appetit");
    else
        printf("%d",anna_share - correct_share);
    return 0;
}
