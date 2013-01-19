#include <stdint.h>

#include "core/dvm.h"
#include "core/vmbase.h"
#include "tests/min_unit.h"
#include "tests/test_system_overrides.h"

static char * test_dvm_creation() {
    DVM dvm = setup_diddy();

    mu_assert("Error: DVM object not created correctly", dvm->running == 1);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_nop() {
    DVM dvm = setup_diddy();

    nop(dvm, 0);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_push_data() {
    DVM dvm = setup_diddy();

    push(dvm, DATA_FLAG | 10);

    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack value at 0 should be 10", dvm->stack[0] == 10);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_push_stack() {
    DVM dvm = setup_diddy();

    push(dvm, DATA_FLAG | 10);

    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack value at 0 should be 10", dvm->stack[0] == 10);
    push(dvm, 0);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack value at 0 should be 10", dvm->stack[0] == 10);
    mu_assert("Error: position counter must be 3", dvm->position == 3);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_push_pointer() {
    DVM dvm = setup_diddy();

    setMem(dvm, 4, 15);

    push(dvm, DATA_FLAG | POINTER_FLAG | 4);

    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack value at 0 should be 10", dvm->stack[0] == 15);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_pop() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 1);
    push_stack(dvm, 2);
    push_stack(dvm, 3);

    pop(dvm, 1);
    pop(dvm, 2);
    pop(dvm, 3);

    mu_assert("Error: memory location 1 must be 3", dvm->ram[1] == 3);
    mu_assert("Error: memory location 2 must be 2", dvm->ram[2] == 2);
    mu_assert("Error: memory location 3 must be 1", dvm->ram[3] == 1);
    mu_assert("Error: position counter must be 4", dvm->position == 4);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_jump_data() {
    DVM dvm = setup_diddy();

    jump(dvm, DATA_FLAG | 10);
    mu_assert("Error: position counter must be 10", dvm->position == 10);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_jump_stack() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 15);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    jump(dvm, 0);
    mu_assert("Error: Stack poition should be -1", dvm->stack_position == -1);
    mu_assert("Error: position counter must be 15", dvm->position == 15);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_jump_pointer() {
    DVM dvm = setup_diddy();

    setMem(dvm, 4, 10);
    push_stack(dvm, 4);
    jump(dvm, POINTER_FLAG);
    mu_assert("Error: position counter must be 10", dvm->position == 10);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_branch_true_data() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 1);
    branch(dvm, DATA_FLAG | 15);
    mu_assert("Error: Stack poition should be -1", dvm->stack_position == -1);
    mu_assert("Error: position counter must be 15", dvm->position == 15);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_branch_true_stack() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 15);
    push_stack(dvm, 1);
    branch(dvm, 0);
    mu_assert("Error: Stack poition should be -1", dvm->stack_position == -1);
    mu_assert("Error: position counter must be 15", dvm->position == 15);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_branch_true_data_pointer() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 1);
    setMem(dvm, 15, 10);
    branch(dvm, DATA_FLAG | POINTER_FLAG | 15);
    mu_assert("Error: Stack poition should be -1", dvm->stack_position == -1);
    mu_assert("Error: position counter must be 10", dvm->position == 10);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_branch_true_stack_pointer() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 10);
    push_stack(dvm, 1);
    setMem(dvm, 10, 15);
    branch(dvm, POINTER_FLAG | 0);
    mu_assert("Error: Stack poition should be -1", dvm->stack_position == -1);
    mu_assert("Error: position counter must be 15", dvm->position == 15);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_branch_false() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 0);
    branch(dvm, 0);
    mu_assert("Error: Stack poition should be -1", dvm->stack_position == -1);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_equal_data_true() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 4);
    equal(dvm, DATA_FLAG | 4);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 1", dvm->stack[0] == 1);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_equal_stack_true() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 4);
    push_stack(dvm, 4);
    equal(dvm, 0);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 1", dvm->stack[0] == 1);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_equal_data_false() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 5);
    equal(dvm, DATA_FLAG | 4);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 0", dvm->stack[0] == 0);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_equal_stack_false() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 4);
    push_stack(dvm, 5);
    equal(dvm, 0);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 0", dvm->stack[0] == 0);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_greater_data_true() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 4);
    greater(dvm, DATA_FLAG | 3);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 1", dvm->stack[0] == 1);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_greater_stack_true() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 3);
    push_stack(dvm, 4);
    greater(dvm, 0);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 1", dvm->stack[0] == 1);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_greater_data_false() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 3);
    greater(dvm, DATA_FLAG | 4);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 0", dvm->stack[0] == 0);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_greater_stack_false() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 4);
    push_stack(dvm, 3);
    greater(dvm, 0);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 0", dvm->stack[0] == 0);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_lesser_data_true() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 3);
    lesser(dvm, DATA_FLAG | 4);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 1", dvm->stack[0] == 1);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_lesser_stack_true() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 4);
    push_stack(dvm, 3);
    lesser(dvm, 0);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 1", dvm->stack[0] == 1);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_lesser_data_false() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 4);
    lesser(dvm, DATA_FLAG | 3);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 0", dvm->stack[0] == 0);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_lesser_stack_false() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 3);
    push_stack(dvm, 4);
    lesser(dvm, 0);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 0", dvm->stack[0] == 0);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_add_data() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 4);
    add(dvm, DATA_FLAG | 3);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 7", dvm->stack[0] == 7);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_add_stack() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 4);
    push_stack(dvm, 3);
    add(dvm, 0);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 7", dvm->stack[0] == 7);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_subtract_data() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 4);
    subtract(dvm, DATA_FLAG | 3);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 1", dvm->stack[0] == 1);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_subtract_stack() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 3);
    push_stack(dvm, 4);
    subtract(dvm, 0);
    mu_assert("Error: Stack poition should be 0", dvm->stack_position == 0);
    mu_assert("Error: Stack top should equal 1", dvm->stack[0] == 1);
    mu_assert("Error: position counter must be 2", dvm->position == 2);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_output_stack() {
    DVM dvm = setup_diddy();
    putchar(0);

    push_stack(dvm, 3);
    output(dvm, 0);

    int sent = getchar();
    mu_assert("Error: DVM sent should be 3", sent == 3);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_output_data() {
    DVM dvm = setup_diddy();
    putchar(0);

    output(dvm, DATA_FLAG | 3);

    int sent = getchar();
    mu_assert("Error: DVM sent should be 3", sent == 3);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_output_stack_pointer() {
    DVM dvm = setup_diddy();
    putchar(0);

    setMem(dvm, 10, 5);
    push_stack(dvm, 10);
    output(dvm, POINTER_FLAG | 0);

    int sent = getchar();
    mu_assert("Error: DVM sent should be 5", sent == 5);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_output_data_pointer() {
    DVM dvm = setup_diddy();
    putchar(0);

    setMem(dvm, 10, 5);
    output(dvm, DATA_FLAG | POINTER_FLAG | 10);

    int sent = getchar();
    mu_assert("Error: DVM sent should be 5", sent == 5);

    cleanup_dvm(dvm);
    return 0;
}


static char * test_dvm_halt_stack() {
    DVM dvm = setup_diddy();

    push_stack(dvm, 3);
    mu_assert("Error: DVM status should be 0", dvm->status == 0);
    mu_assert("Error: DVM should be running", dvm->running == 1);
    halt(dvm, 0);
    mu_assert("Error: DVM status should be 3", dvm->status == 3);
    mu_assert("Error: DVM should not be running", dvm->running == 0);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_halt_data() {
    DVM dvm = setup_diddy();

    mu_assert("Error: DVM status should be 0", dvm->status == 0);
    mu_assert("Error: DVM should be running", dvm->running == 1);
    halt(dvm, DATA_FLAG | 3);
    mu_assert("Error: DVM status should be 3", dvm->status == 3);
    mu_assert("Error: DVM should not be running", dvm->running == 0);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_halt_stack_pointer() {
    DVM dvm = setup_diddy();

    setMem(dvm, 10, 5);
    push_stack(dvm, 10);
    mu_assert("Error: DVM status should be 0", dvm->status == 0);
    mu_assert("Error: DVM should be running", dvm->running == 1);
    halt(dvm, POINTER_FLAG | 0);
    mu_assert("Error: DVM status should be 5", dvm->status == 5);
    mu_assert("Error: DVM should not be running", dvm->running == 0);

    cleanup_dvm(dvm);
    return 0;
}

static char * test_dvm_halt_data_pointer() {
    DVM dvm = setup_diddy();

    setMem(dvm, 10, 5);
    mu_assert("Error: DVM status should be 0", dvm->status == 0);
    mu_assert("Error: DVM should be running", dvm->running == 1);
    halt(dvm, DATA_FLAG | POINTER_FLAG | 10);
    mu_assert("Error: DVM status should be 5", dvm->status == 5);
    mu_assert("Error: DVM should not be running", dvm->running == 0);

    cleanup_dvm(dvm);
    return 0;
}

char * test_dvm() {

    mu_run_test(test_dvm_creation);
    mu_run_test(test_dvm_nop);
    mu_run_test(test_dvm_push_data);
    mu_run_test(test_dvm_push_stack);
    mu_run_test(test_dvm_push_pointer);
    mu_run_test(test_dvm_pop);
    mu_run_test(test_dvm_jump_data);
    mu_run_test(test_dvm_jump_stack);
    mu_run_test(test_dvm_jump_pointer);
    mu_run_test(test_dvm_branch_true_data);
    mu_run_test(test_dvm_branch_true_stack);
    mu_run_test(test_dvm_branch_true_data_pointer);
    mu_run_test(test_dvm_branch_true_stack_pointer);
    mu_run_test(test_dvm_branch_false);
    mu_run_test(test_dvm_equal_data_true);
    mu_run_test(test_dvm_equal_stack_true);
    mu_run_test(test_dvm_equal_data_false);
    mu_run_test(test_dvm_equal_stack_false);
    mu_run_test(test_dvm_greater_data_true);
    mu_run_test(test_dvm_greater_stack_true);
    mu_run_test(test_dvm_greater_data_false);
    mu_run_test(test_dvm_greater_stack_false);
    mu_run_test(test_dvm_lesser_data_true);
    mu_run_test(test_dvm_lesser_stack_true);
    mu_run_test(test_dvm_lesser_data_false);
    mu_run_test(test_dvm_lesser_stack_false);
    mu_run_test(test_dvm_add_data);
    mu_run_test(test_dvm_add_stack);
    mu_run_test(test_dvm_subtract_data);
    mu_run_test(test_dvm_subtract_stack);
    mu_run_test(test_dvm_output_stack);
    mu_run_test(test_dvm_output_data);
    mu_run_test(test_dvm_output_stack_pointer);
    mu_run_test(test_dvm_output_data_pointer);
    mu_run_test(test_dvm_halt_stack);
    mu_run_test(test_dvm_halt_data);
    mu_run_test(test_dvm_halt_stack_pointer);
    mu_run_test(test_dvm_halt_data_pointer);

    return 0;
}

