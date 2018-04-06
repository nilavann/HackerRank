#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int camelcase(char* s) {
    // Complete this function
    int words = 0;
    for(int i = 0; i < strlen(s); i++){
        int ascii = s[i];
        if(ascii >= 65 && ascii <= 90)
            words++;
    }
    return words + 1;
}

int main() {
    char* s = (char *)malloc(512000 * sizeof(char));
    scanf("%s", s);
    int result = camelcase(s);
    printf("%d\n", result);
    return 0;
}
