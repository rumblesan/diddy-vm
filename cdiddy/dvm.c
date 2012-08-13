#include "dvm.h"
#include "vmbase.h"

DVM setup_diddyvm() {

    DVM dvm = setup_vmbase();

    dvm->instructions[0] = nop;
    dvm->instructions[0] = copy;
    dvm->instructions[0] = jump;
    dvm->instructions[0] = branch;
    dvm->instructions[0] = equal;
    dvm->instructions[0] = greater;
    dvm->instructions[0] = lesser;
    dvm->instructions[0] = add;
    dvm->instructions[0] = subtract;
    dvm->instructions[0] = output;
    dvm->instructions[0] = halt;

    return dvm;
}

void nop(DVM dvm) {
    next(dvm);
}


void copy(DVM dvm) {
    next(dvm);
    int inAddr = getMem(dvm, -1);
    int inVal = getMem(dvm, inAddr);
    next(dvm);
    int outAddr = getMem(dvm, -1);
    setMem(dvm, outAddr, inVal);
    next(dvm);
}

void jump(DVM dvm) {
    next(dvm);
    int inAddr = getMem(dvm, -1);
    set_instruction_pointer(dvm, inAddr);
}

void branch(DVM dvm) {
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

void equal(DVM dvm) {
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

void greater(DVM dvm) {
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

void lesser(DVM dvm) {
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

void add(DVM dvm) {
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

void subtract(DVM dvm) {
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

void output(DVM dvm) {
    next(dvm);
    int aAddr = getMem(dvm, -1);
    int aVal = getMem(dvm, aAddr);

    system_out(dvm, aVal);
}

void halt(DVM dvm) {
    next(dvm);
    int aAddr = getMem(dvm, -1);
    int aVal = getMem(dvm, aAddr);

    system_exit(dvm, aVal);
}


int main(int argc, char *argv[]) {
    DVM dvm = (DVM) setup_diddyvm();
    next(dvm);
    next(dvm);
    cleanup_dvm(dvm);

    return 0;
}

