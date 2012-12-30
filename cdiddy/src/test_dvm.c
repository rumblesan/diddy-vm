#include <stdint.h>

#include "dvm.h"
#include "vmbase.h"
#include "min_unit.h"

static char * test_dvm_creation() {
    DVM dvm = setup_diddy();

    mu_assert("Error: DVM object not created correctly", dvm->running == 1);

    cleanup_dvm(dvm);
    return 0;
}


char * test_dvm() {

    mu_run_test(test_dvm_creation);

    return 0;
}

