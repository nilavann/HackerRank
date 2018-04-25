#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        int n; 
        int k; 
        scanf("%d %d",&n,&k);
        if( ((k - 1)|k) > n && k % 2 ==0)
            printf("%d\n", k - 2);
        else
            printf("%d\n", k - 1);
    }
    return 0;
}
