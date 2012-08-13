#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "vmbase.h"

DVM setup_vmbase() {

    DVM dvm           = (DVM) malloc(sizeof(DVM_Data));

    dvm->ram          = (int*) malloc(sizeof(int*) * 4096);

    int i;
    for (i=0; i < 4096; i++) {
        dvm->ram[i] = 0;
    }

    dvm->position     = 1;
    dvm->running      = 1;
    dvm->status       = 0;
    return dvm;
}

void execute_next_instruction(DVM dvm) {
    int i = getMem(dvm, -1);
    (*dvm->instructions[i]) (dvm);
}

void set_instruction_pointer(DVM dvm, int address) {
    dvm->position = address;
}

void next(DVM dvm) {
    dvm->position++;
}

int getMem(DVM dvm, int addr) {

    int output;

    if (addr == -1) {
        output = dvm->ram[dvm->position];
    } else {
        output = dvm->ram[addr];
    }
    return output;
}

void setMem(DVM dvm, int addr, int value) {
    dvm->ram[addr] = value;
}

void system_exit(DVM dvm, int value) {
    dvm->running = 0;
    dvm->status = value;
}

void system_out(DVM dvm, int c) {
    putchar(c);
}

void load_program(DVM dvm, char *program_data) {
}

void cleanup_dvm(DVM dvm) {
    free(dvm->ram);
    free(dvm);
}

/*
int main(int argc, char *argv[]) {
    DVM dvm = (DVM) setup_vmbase();
    next(dvm);
    next(dvm);
    cleanup_dvm(dvm);

    return 0;
}
*/


