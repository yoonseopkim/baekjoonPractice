#include <stdio.h>
#include <math.h>
#define PI 3.141592
int main(void)
    {
        int a,b,c;
        scanf("%d %d", &a, &b);
        if(a>b) {
            printf(">\n");
        }
        else if(a<b) {
            printf("<\n");
        }
        else {
            printf("==\n");
        }


}

