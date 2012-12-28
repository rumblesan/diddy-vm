#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>

#include "vmbase.h"

#define INSTRUCTION_MASK (31 << 28)

DVM setup_vmbase() {

    DVM dvm             = (DVM) malloc(sizeof(DVM_Data));

    dvm->ram_size       = 4096;
    dvm->position       = 1;
    dvm->ram            = (uint32_t*) malloc(sizeof(uint32_t*) * dvm->ram_size);

    dvm->stack_size     = 1024;
    dvm->stack_position = -1;
    dvm->stack          = (uint32_t*) malloc(sizeof(uint32_t*) * dvm->stack_size);

    int i;
    for (i=0; i < 4096; i++) {
        dvm->ram[i] = 0;
    }

    dvm->running        = 1;
    dvm->status         = 0;

    dvm->program_length = 0;

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

void push_stack(DVM dvm, uint32_t data) {
    dvm->stack_position++;
    if (dvm->stack_position == dvm->stack_size) {
        dvm->running = 0;
        dvm->status = 1;
    } else {
        dvm->stack[dvm->stack_position] = data;
    }
}

uint32_t pop_stack(DVM dvm) {
    uint32_t value = 0;
    if (dvm->stack_position < 0) {
        dvm->running = 0;
        dvm->status = 1;
    } else {
        value = dvm->stack[dvm->stack_position];
    }
    dvm->stack_position--;
    return value;
}

uint32_t getMem(DVM dvm, int addr) {

    uint32_t output;

    if (addr == -1) {
        output = dvm->ram[dvm->position];
    } else {
        output = dvm->ram[addr];
    }
    return output;
}

void setMem(DVM dvm, int addr, uint32_t value) {
    dvm->ram[addr] = value;
}

void system_exit(DVM dvm, int value) {
    dvm->running = 0;
    dvm->status = value;
}

void system_out(DVM dvm, int c) {
    putchar(c);
    next(dvm);
}

void load_program(DVM dvm, uint32_t *program_data, int length) {

    int i;
    for (i = 0; i < length; i++) {
        setMem(dvm, dvm->position, program_data[i]);
        next(dvm);
    }
    dvm->program_length = length;
    set_instruction_pointer(dvm, 1);
}

void dump_program(DVM dvm) {
    int i;
    for (i = 0; i < dvm->program_length; i++) {
        printf("%i\n", getMem(dvm, i));
    }
}

void cleanup_dvm(DVM dvm) {
    free(dvm->ram);
    free(dvm);
}

