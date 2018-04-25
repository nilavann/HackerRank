#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int aday,amonth,ayear;
    int eday,emonth,eyear;
    scanf("%d%d%d",&aday,&amonth,&ayear);
    scanf("%d%d%d",&eday,&emonth,&eyear);
    int fine = 0;
    if( ayear > eyear)
        fine = 10000;
    else{
        if( amonth > emonth && ayear == eyear)
            fine = (amonth - emonth) * 500;
        else{
            if( aday > eday && ayear == eyear && amonth == emonth)
                fine = (aday - eday) * 15;
        }
    }
    printf("%d",fine);
    return 0;
}
