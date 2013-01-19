#include <stdint.h>

#include "core/dvm.h"
#include "core/vmbase.h"
#include "tests/min_unit.h"
#include "tests/test_system_overrides.h"

static char * test_creation() {
    DVM dvm = setup_vmbase();

    mu_assert("Error: DVM object not created correctly", dvm->running == 1);

    cleanup_dvm(dvm);
    return 0;
}

static void stop_func(DVM dvm, uint32_t bits) {
    dvm->running = 0;
}

static char * test_execute_next_instruction() {
    DVM dvm = setup_vmbase();

    dvm->instructions[1] = stop_func;
    dvm->position = 100;
    dvm->ram[100] = 1 << 28;
    mu_assert("Error: DVM should be running", dvm->running == 1);
    execute_next_instruction(dvm);

    mu_assert("Error: DVM should not be running", dvm->running == 0);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_set_instruction_pointer() {
    DVM dvm = setup_vmbase();

    mu_assert("Error: instruction pointer should be 1", dvm->position == 1);
    set_instruction_pointer(dvm, 100);
    mu_assert("Error: instruction pointer should be 100", dvm->position == 100);
    set_instruction_pointer(dvm, 200);
    mu_assert("Error: instruction pointer should be 200", dvm->position == 200);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_next_instruction_pointer() {
    DVM dvm = setup_vmbase();

    mu_assert("Error: instruction pointer should be 1", dvm->position == 1);
    next(dvm);
    mu_assert("Error: instruction pointer should be 2", dvm->position == 2);
    next(dvm);
    mu_assert("Error: instruction pointer should be 3", dvm->position == 3);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_load_program() {
    DVM dvm = setup_vmbase();

    uint32_t program_data[4] = {1, 2, 3, 4};

    load_program(dvm, program_data, 4);

    mu_assert("Error: memory value should be 1", dvm->ram[1] == 1);
    mu_assert("Error: memory value should be 2", dvm->ram[2] == 2);
    mu_assert("Error: memory value should be 3", dvm->ram[3] == 3);
    mu_assert("Error: memory value should be 4", dvm->ram[4] == 4);
    mu_assert("Error: instruction pointer should be 1", dvm->position == 1);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_stack() {
    DVM dvm = setup_vmbase();

    mu_assert("Error: Stack poition should be -1", dvm->stack_position == -1);
    push_stack(dvm, 0);
    push_stack(dvm, 1);
    push_stack(dvm, 2);
    mu_assert("Error: Stack poition should be 2", dvm->stack_position == 2);

    mu_assert("Error: Popped value should be 2", pop_stack(dvm) == 2);
    mu_assert("Error: Popped value should be 1", pop_stack(dvm) == 1);
    mu_assert("Error: Popped value should be 0", pop_stack(dvm) == 0);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_set_mem() {
    DVM dvm = setup_vmbase();

    setMem(dvm, 10, 100);
    setMem(dvm, 20, 200);

    mu_assert("Error: DVM memory not set correctly", dvm->ram[10] == 100);
    mu_assert("Error: DVM memory not set correctly", dvm->ram[20] == 200);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_get_mem() {
    DVM dvm = setup_vmbase();

    dvm->ram[10] = 100;
    dvm->ram[20] = 200;

    mu_assert("Error: getMem not returning correct value", getMem(dvm, 10) == 100);
    mu_assert("Error: getMem not returning correct value", getMem(dvm, 20) == 200);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_get_pointer_mem() {
    DVM dvm = setup_vmbase();

    dvm->ram[200] = 200;
    dvm->ram[201] = 201;
    dvm->ram[202] = 202;

    set_instruction_pointer(dvm, 200);
    mu_assert("Error: getMem not returning correct value", getMem(dvm, -1) == 200);
    next(dvm);
    mu_assert("Error: getMem not returning correct value", getMem(dvm, -1) == 201);
    next(dvm);
    mu_assert("Error: getMem not returning correct value", getMem(dvm, -1) == 202);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_exit() {
    DVM dvm = setup_vmbase();

    system_exit(dvm, 5);
    mu_assert("Error: DVM running should be 0", dvm->running == 0);
    mu_assert("Error: DVM status should be 5", dvm->status == 5);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_system_out() {
    DVM dvm = setup_vmbase();

    system_out(dvm, 5);
    mu_assert("Error: DVM status should be running", dvm->running == 1);

    cleanup_dvm(dvm);
    return 0;
}

char * test_vmbase() {
    mu_run_test(test_creation);
    mu_run_test(test_execute_next_instruction);
    mu_run_test(test_set_instruction_pointer);
    mu_run_test(test_next_instruction_pointer);
    mu_run_test(test_stack);
    mu_run_test(test_get_mem);
    mu_run_test(test_get_pointer_mem);
    mu_run_test(test_set_mem);
    mu_run_test(test_exit);
    mu_run_test(test_system_out);
    mu_run_test(test_load_program);
    return 0;
}

