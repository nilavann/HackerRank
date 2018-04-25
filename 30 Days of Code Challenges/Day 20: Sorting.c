#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
    int n; 
    scanf("%d", &n);
    int *a = malloc(sizeof(int) * n);
    for(int a_i = 0; a_i < n; a_i++){
       scanf("%d",&a[a_i]);
    }
    // Write Your Code Here
    int numberofswap = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1; j++) {
            if (a[j] > a[j + 1]) {
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                numberofswap++;
            }
        }
        if (numberofswap == 0)
            break;
    }
    printf("Array is sorted in %d swaps.\nFirst Element: %d\nLast Element: %d\n", numberofswap, a[0], a[n - 1]);
    return 0;
}
