/* chap16/equal2.c */
#include <stdio.h>

int main(void) {
    /* declaration of two variables of different types */
    char a_string;
    int an_int;

    /* initialization of the values of these variables */
    a_string = 'A';
    an_int = 65;

    printf("Does C think these two objects are equal? %d\n", a_string == an_int);

    return 0;
}