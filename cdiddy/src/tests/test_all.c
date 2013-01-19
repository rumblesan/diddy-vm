#include <stdio.h>

#include "tests/min_unit.h"
#include "tests/test_vmbase.h"
#include "tests/test_dvm.h"

int tests_run;

int main(int argc, char *argv[]) {

    printf("\n");
    printf("*****************\n");
    printf("* Running tests *\n");
    printf("*****************\n\n");

    int result = 0;

    tests_run = 0;
    char *vmbase_results = test_vmbase();
    if (vmbase_results != 0) {
        printf("%s\n", vmbase_results);
    } else {
        printf("VMBASE TESTS PASSED\n");
    }
    printf("    Tests run: %d\n", tests_run);
    printf("\n");

    result = result || (vmbase_results != 0);

    tests_run = 0;
    char *dvm_results = test_dvm();
    if (dvm_results != 0) {
        printf("%s\n", dvm_results);
    } else {
        printf("DVM TESTS PASSED\n");
    }
    printf("    Tests run: %d\n", tests_run);
    printf("\n");

    result = result || (dvm_results != 0);

    return result;
}


