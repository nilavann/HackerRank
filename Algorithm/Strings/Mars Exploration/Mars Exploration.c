#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int marsExploration(char* s) {
    // Complete this function
    char sos[] = "SOS";
    int count = 0;
    for(int i =0; i < strlen(s) / 3; i++){
        for(int j = 0; j < 3; j++){
            if(s[(i * 3) + j] != sos[j])
                 count++; 
        }
    }
    return count;
}

int main() {
    char* s = (char *)malloc(512000 * sizeof(char));
    scanf("%s", s);
    int result = marsExploration(s);
    printf("%d\n", result);
    return 0;
}
