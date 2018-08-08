#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int buffer = 100;
    char ch, s[buffer], sen[buffer];
    scanf("%c", &ch);
    scanf("%s", s);
    // leave space to ignore the newline from pre input
    scanf(" %[^\n]%*c", sen);
    printf("%c\n%s\n%s", ch, s, sen);
    return 0;
}