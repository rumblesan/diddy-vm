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

void nop(DVM dvm, uint32_t data) {
    next(dvm);
}

void push(DVM dvm, uint32_t data) {
}

void pop(DVM dvm, uint32_t data) {
}

void jump(DVM dvm, uint32_t data) {
    next(dvm);
    int inAddr = getMem(dvm, -1);
    set_instruction_pointer(dvm, inAddr);
}

void branch(DVM dvm, uint32_t data) {
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

void equal(DVM dvm, uint32_t data) {
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

void greater(DVM dvm, uint32_t data) {
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

void lesser(DVM dvm, uint32_t data) {
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

void add(DVM dvm, uint32_t data) {
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

void subtract(DVM dvm, uint32_t data) {
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

void output(DVM dvm, uint32_t data) {
    next(dvm);
    int aAddr = getMem(dvm, -1);
    int aVal = getMem(dvm, aAddr);

    system_out(dvm, aVal);
    next(dvm);
}

void halt(DVM dvm, uint32_t data) {
    next(dvm);
    int aAddr = getMem(dvm, -1);
    int aVal = getMem(dvm, aAddr);

    system_exit(dvm, aVal);
}

