#include <stdint.h>

#include "dvm.h"
#include "vmbase.h"

#define DATA_FLAG 0x08000000
#define POINTER_FLAG 0x04000000
#define DATA_MASK  0x03FFFFFF

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
    next(dvm);
    int inAddr = getMem(dvm, -1);
    set_instruction_pointer(dvm, inAddr);
}

void branch(DVM dvm, uint32_t bits) {
    next(dvm);
    int aAddr = getMem(dvm, -1);
    int aVal = getMem(dvm, aAddr);

    next(dvm);
    int bAddr = getMem(dvm, -1);

    next(dvm);
    int cAddr = getMem(dvm, -1);

    if (aVal == 0) {
        set_instruction_pointer(dvm, cAddr);
    } else {
        set_instruction_pointer(dvm, bAddr);
    }
}

void equal(DVM dvm, uint32_t bits) {
    next(dvm);
    int aAddr = getMem(dvm, -1);
    int aVal = getMem(dvm, aAddr);

    next(dvm);
    int bAddr = getMem(dvm, -1);
    int bVal = getMem(dvm, bAddr);

    next(dvm);
    int cAddr = getMem(dvm, -1);

    if (aVal == bVal) {
        setMem(dvm, cAddr, 1);
    } else {
        setMem(dvm, cAddr, 0);
    }
    next(dvm);
}

void greater(DVM dvm, uint32_t bits) {
    next(dvm);
    int aAddr = getMem(dvm, -1);
    int aVal = getMem(dvm, aAddr);

    next(dvm);
    int bAddr = getMem(dvm, -1);
    int bVal = getMem(dvm, bAddr);

    next(dvm);
    int cAddr = getMem(dvm, -1);

    if (aVal > bVal) {
        setMem(dvm, cAddr, 1);
    } else {
        setMem(dvm, cAddr, 0);
    }
    next(dvm);
}

void lesser(DVM dvm, uint32_t bits) {
    next(dvm);
    int aAddr = getMem(dvm, -1);
    int aVal = getMem(dvm, aAddr);

    next(dvm);
    int bAddr = getMem(dvm, -1);
    int bVal = getMem(dvm, bAddr);

    next(dvm);
    int cAddr = getMem(dvm, -1);

    if (aVal < bVal) {
        setMem(dvm, cAddr, 1);
    } else {
        setMem(dvm, cAddr, 0);
    }
    next(dvm);
}

void add(DVM dvm, uint32_t bits) {
    next(dvm);
    int aAddr = getMem(dvm, -1);
    int aVal = getMem(dvm, aAddr);

    next(dvm);
    int bAddr = getMem(dvm, -1);
    int bVal = getMem(dvm, bAddr);

    next(dvm);
    int cAddr = getMem(dvm, -1);

    int value = aVal + bVal;

    setMem(dvm, cAddr, value);
    next(dvm);
}

void subtract(DVM dvm, uint32_t bits) {
    next(dvm);
    int aAddr = getMem(dvm, -1);
    int aVal = getMem(dvm, aAddr);

    next(dvm);
    int bAddr = getMem(dvm, -1);
    int bVal = getMem(dvm, bAddr);

    next(dvm);
    int cAddr = getMem(dvm, -1);

    int value = aVal - bVal;

    setMem(dvm, cAddr, value);
    next(dvm);
}

void output(DVM dvm, uint32_t bits) {
    next(dvm);
    int aAddr = getMem(dvm, -1);
    int aVal = getMem(dvm, aAddr);

    system_out(dvm, aVal);
    next(dvm);
}

void halt(DVM dvm, uint32_t bits) {
    next(dvm);
    int aAddr = getMem(dvm, -1);
    int aVal = getMem(dvm, aAddr);

    system_exit(dvm, aVal);
}

