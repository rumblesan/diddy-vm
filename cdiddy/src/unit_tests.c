#include <stdio.h>
#include <stdint.h>

#define mu_assert(message, test) do { if (!(test)) return message; } while (0)
#define mu_run_test(test) do { char *message = test(); tests_run++; \
                               if (message) return message; } while (0)

#include "dvm.h"
#include "vmbase.h"

int tests_run = 0;

static char * test_creation() {
    DVM vmbase = setup_vmbase();
    mu_assert("Error: DVM object not created correctly", vmbase->running == 1);
    return 0;
}

static char * all_tests() {
    mu_run_test(test_creation);
    return 0;
}

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

