#include <stdio.h>
#include <stdint.h>

#include "min_unit.h"
#include "unit_tests.h"


int tests_run = 0;



int main(int argc, char *argv[]) {
    char *result = all_tests();
    if (result != 0) {
        printf("%s\n", result);
    } else {
        printf("ALL TESTS PASSED\n");
    }
    printf("Tests run: %d\n", tests_run);

    return result != 0;
}


