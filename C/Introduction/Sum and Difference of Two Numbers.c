#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int num1, num2;
    float f1, f2;
	scanf("%d %d",&num1, &num2);
    scanf("%f %f",&f1, &f2);
    printf("%d %d\n", num1 + num2, num1 - num2);
    printf("%.1f %.1f", f1 + f2, f1 - f2);
    return 0;
}