#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

char* create_unique_string(char* s, int length){
    int index = 0, flag;
    char* unique = (char *)malloc( length * sizeof( char));
    unique[0] = s[0];
    for( int i = 0; i < length; i++){
        flag = 0;
        for( int j = 0; j <= index; j++){
            if( unique[j] == s[i]){
                flag = 1;
                break;
            }
        }
        if( flag == 0){
            unique[++index] = s[i];
        }
            
    }
    unique[++index] = '\0';
    return unique;
}
int twoCharaters(char* s) {
    // Complete this function
    int length = strlen(s);
    int index, max = 0,flag;
    //get unique elements in given string
    char* unique = create_unique_string(s, length);
    int uniquelength = strlen(unique);
    
    for( int i = 0; i < uniquelength; i++){
        for( int j = 0; j < uniquelength; j++){
            index = -1;
            //check for same char
            if( j == i)
                continue;
            //else make new string
            else{
                char* newstring = (char *)malloc(length * sizeof( char));
                for( int k = 0; k < length; k++){
                    if( s[k] == unique[i] || s[k] == unique[j])
                        newstring[++index] = s[k];
                }
            newstring[++index] = '\0';
            int new_string_length = strlen(newstring);
            flag = 0;
            //check weather it is str of alternating char
            for( int l = 0; l < new_string_length - 1; l++){
                if( newstring[l] == newstring[l + 1]){
                    flag = 1;
                    break;
                }
            }
            if( flag == 0){
                if( new_string_length > max)
                    max = new_string_length;
            }
            }
        }
    }
    return max;
}

int main() {
    int l; 
    scanf("%i", &l);
    char* s = (char *)malloc(512000 * sizeof(char));
    scanf("%s", s);
    int result = twoCharaters(s);
    printf("%d\n", result);
    return 0;
}
