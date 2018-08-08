#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
    //Write your code here.
    int maxand = 0, maxor = 0, maxxor = 0;
    for( int i = 1; i < n; i++){
        for( int j = i + 1; j <= n; j++){
            int ans = i & j;
            if( ans < k && ans > maxand)
                maxand = ans;
            ans = i | j;
            if( ans < k && ans > maxor)
                maxor = ans;
            ans = i ^ j;
            if( ans < k && ans > maxxor)
                maxxor = ans;
        }
    }
    printf("%d\n%d\n%d", maxand, maxor, maxxor);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
