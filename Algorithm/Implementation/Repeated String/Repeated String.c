#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
int count_a(char* str){
    int count = 0;
    for( int i = 0; i < strlen(str); i++){
        if( str[i] == 'a')
            count++;
    }
    return count;
}
long int repeatedString(char* s, long int n) {
    // Complete this function
    int length = strlen(s);
    int count = count_a(s);
    // full string occurance 
    long int occurance = ( n / length) * count;
    char* str = (char *)malloc(( n % length) * sizeof(char));
    //remaining string
    for( int i = 0; i < n % length; i++){
        str[i] = s[i];
    }
    occurance += count_a(str);
    return occurance;
}

int main() {
    char* s = (char *)malloc(512000 * sizeof(char));
    scanf("%s", s);
    long int n; 
    scanf("%li", &n);
    long int result = repeatedString(s, n);
    printf("%ld\n", result);
    return 0;
}
