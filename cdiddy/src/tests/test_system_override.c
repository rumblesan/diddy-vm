#include <stdio.h>

static int gc;

// overriding the putchar function so I
// can test without having text written out
int putchar(int c) {
    gc = c;
    return 0;
}

int getchar() {
    return gc;
}

