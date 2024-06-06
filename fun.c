/* chap16/fun.c */
/* NOT EXECUTABLE since it C code, not Python */
#include <stdio.h>

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