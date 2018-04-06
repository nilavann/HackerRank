#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

char* super_reduced_string(char* s){
    // Complete this function
    for(int i = 0; i < strlen(s);){
        //check pre char is same as present
        if(s[i] == s[i - 1]){
            i--;
        }
        //check current and next char same if remove them
        else if(s[i] == s[i + 1]){
            int k = i; 
            for(int j = i + 2;j < strlen(s); j++,k++)
                s[k] = s[j];
            s[k] = '\0';
        }else
            i++;
    }
    if(strlen(s) == 0)
        return "Empty String";
    else
        return s;
}

int main() {
    char* s = (char *)malloc(512000 * sizeof(char));
    scanf("%s", s);
    int result_size;
    char* result = super_reduced_string(s);
    printf("%s\n", result);
    return 0;
}