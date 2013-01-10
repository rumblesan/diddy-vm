#ifndef VMBASE_H
#define VMBASE_H

#include <stdint.h>

typedef struct diddyvm *DVM;
typedef struct diddyvm {

    int ram_size;
    int position;
    uint32_t *ram;

    int stack_size;
    int stack_position;
    uint32_t *stack;

    // Create an array that will store function pointers
    void (*instructions[12]) (DVM dvm, uint32_t data);

    int running;

    int status;

    int program_length;

} DVM_Data;

DVM setup_vmbase();

void execute_next_instruction(DVM dvm);

void set_instruction_pointer(DVM dvm, int address);

void next(DVM dvm);

void push_stack(DVM dvm, uint32_t data);

uint32_t pop_stack(DVM dvm);

uint32_t getMem(DVM dvm, int addr);

void setMem(DVM dvm, int addr, uint32_t value);

void system_exit(DVM dvm, int value);

void system_out(DVM dvm, int c);

void load_program(DVM dvm, uint32_t *program_data, int length);

void dump_program(DVM dvm);

void cleanup_dvm(DVM dvm);

#endif
