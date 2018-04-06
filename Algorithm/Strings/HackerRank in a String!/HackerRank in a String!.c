#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

char* hackerrankInString(char* s) {
    // Complete this function
    char* key = "hackerrank";
    int j = 0;
    for( int i = 0; i < strlen(s); i++){
        if( j < 10 && s[i] == key[j])
            j++;
    }
    if( j == 10)
        return "YES";
    else
        return "NO";
}

int main() {
    int q; 
    scanf("%i", &q);
    for(int a0 = 0; a0 < q; a0++){
        char* s = (char *)malloc(512000 * sizeof(char));
        scanf("%s", s);
        int result_size;
        char* result = hackerrankInString(s);
        printf("%s\n", result);
    }
    return 0;
}
