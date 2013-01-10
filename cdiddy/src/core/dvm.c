#include <stdint.h>

#include "dvm.h"
#include "vmbase.h"

DVM setup_diddy() {

    DVM dvm = setup_vmbase();

    dvm->instructions[0] = nop;
    dvm->instructions[1] = push;
    dvm->instructions[2] = pop;
    dvm->instructions[3] = jump;
    dvm->instructions[4] = branch;
    dvm->instructions[5] = equal;
    dvm->instructions[6] = greater;
    dvm->instructions[7] = lesser;
    dvm->instructions[8] = add;
    dvm->instructions[9] = subtract;
    dvm->instructions[10] = output;
    dvm->instructions[11] = halt;

    return dvm;
}

void nop(DVM dvm, uint32_t bits) {
    next(dvm);
}

void push(DVM dvm, uint32_t bits) {
    uint32_t value = 0;
    if (bits & DATA_FLAG) {
        value = bits & DATA_MASK;
    } else {
        value = pop_stack(dvm);
    }
    if (bits & POINTER_FLAG) {
        value = getMem(dvm, value);
    }
    push_stack(dvm, value);
    next(dvm);
}

void pop(DVM dvm, uint32_t bits) {
    setMem(dvm, bits & DATA_MASK, pop_stack(dvm));
    next(dvm);
}

void jump(DVM dvm, uint32_t bits) {
    uint32_t value = 0;
    if (bits & DATA_FLAG) {
        value = bits & DATA_MASK;
    } else {
        value = pop_stack(dvm);
    }
    if (bits & POINTER_FLAG) {
        value = getMem(dvm, value);
    }
    set_instruction_pointer(dvm, value);
}

void branch(DVM dvm, uint32_t bits) {
    if (pop_stack(dvm) != 0) {
        uint32_t value = 0;
        if (bits & DATA_FLAG) {
            value = bits & DATA_MASK;
        } else {
            value = pop_stack(dvm);
        }
        if (bits & POINTER_FLAG) {
            value = getMem(dvm, value);
        }
        set_instruction_pointer(dvm, value);
    } else {
        next(dvm);
    }
}

void equal(DVM dvm, uint32_t bits) {

    uint32_t aVal = pop_stack(dvm);

    uint32_t bVal = 0;
    if (bits & DATA_FLAG) {
        bVal = bits & DATA_MASK;
    } else {
        bVal = pop_stack(dvm);
    }

    if (aVal == bVal) {
        push_stack(dvm, 1);
    } else {
        push_stack(dvm, 0);
    }

    next(dvm);
}

void greater(DVM dvm, uint32_t bits) {

    uint32_t aVal = pop_stack(dvm);

    uint32_t bVal = 0;
    if (bits & DATA_FLAG) {
        bVal = bits & DATA_MASK;
    } else {
        bVal = pop_stack(dvm);
    }

    if (aVal > bVal) {
        push_stack(dvm, 1);
    } else {
        push_stack(dvm, 0);
    }

    next(dvm);
}

void lesser(DVM dvm, uint32_t bits) {

    uint32_t aVal = pop_stack(dvm);

    uint32_t bVal = 0;
    if (bits & DATA_FLAG) {
        bVal = bits & DATA_MASK;
    } else {
        bVal = pop_stack(dvm);
    }

    if (aVal < bVal) {
        push_stack(dvm, 1);
    } else {
        push_stack(dvm, 0);
    }

    next(dvm);
}

void add(DVM dvm, uint32_t bits) {

    uint32_t aVal = pop_stack(dvm);

    uint32_t bVal = 0;
    if (bits & DATA_FLAG) {
        bVal = bits & DATA_MASK;
    } else {
        bVal = pop_stack(dvm);
    }

    push_stack(dvm, aVal + bVal);

    next(dvm);
}

void subtract(DVM dvm, uint32_t bits) {

    uint32_t aVal = pop_stack(dvm);

    uint32_t bVal = 0;
    if (bits & DATA_FLAG) {
        bVal = bits & DATA_MASK;
    } else {
        bVal = pop_stack(dvm);
    }

    push_stack(dvm, aVal - bVal);

    next(dvm);

}

void output(DVM dvm, uint32_t bits) {
    uint32_t value = 0;
    if (bits & DATA_FLAG) {
        value = bits & DATA_MASK;
    } else {
        value = pop_stack(dvm);
    }
    if (bits & POINTER_FLAG) {
        value = getMem(dvm, value);
    }
    system_out(dvm, value);

    next(dvm);
}

void halt(DVM dvm, uint32_t bits) {
    uint32_t value = 0;
    if (bits & DATA_FLAG) {
        value = bits & DATA_MASK;
    } else {
        value = pop_stack(dvm);
    }
    if (bits & POINTER_FLAG) {
        value = getMem(dvm, value);
    }
    system_exit(dvm, value);
}

