/* chap16/equal.c */
#include <stdio.h>

int main(void) {
    char a_string = 'A';
    int an_int = 65;

    printf("Does C think these two objects are equal? %d\n", a_string == an_int);

    return 0;
}