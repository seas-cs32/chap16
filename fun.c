/* chap16/fun.c */
#include <stdio.h>
#include <string.h>

int main(void) {
    char *a = "Hello";
    char *b = "World";
    if (strcmp(a,b) == 0) {
        printf("The strings are the same.\n");
    } else {
        printf("The strings are different.\n");
    }
    return 0;
}
