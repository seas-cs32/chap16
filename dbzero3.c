/* dbzero3.c */
#include <stdio.h>

int main() {
    char answer[10];
    printf("Do you want to divide by zero? (y/n) ");
    fgets(answer, sizeof(answer), stdin);

    if (answer[0] == 'y') {
        int x = 42;
        int q = x / 0;
        printf("%d\n", q);
    }
    else {
        printf("Good call!  I didn't want to do that either.\n");
    }

    return 0;
}
