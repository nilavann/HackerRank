#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    char s[1000];
    int digits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    scanf("%s", s);
    for(int i = 0; i < strlen( s); i++){
        if( s[i] >= '0' && s[i] <= '9')
            digits[ s[i] - '0']++;
    }
    for( int i = 0; i < 10; i++)
        printf("%d ", digits[i]);
    return 0;
}
