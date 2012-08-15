#ifndef VMBASE_H
#define VMBASE_H

typedef struct diddyvm *DVM;
typedef struct diddyvm {

    int *ram;

    // Create an array that will store function pointers
    void (*instructions[11]) (DVM dvm);

    int position;

    int running;

    int status;

    int program_length;

} DVM_Data;

DVM setup_vmbase();

void execute_next_instruction(DVM dvm);

void set_instruction_pointer(DVM dvm, int address);

void next(DVM dvm);

int getMem(DVM dvm, int addr);

void setMem(DVM dvm, int addr, int value);

void system_exit(DVM dvm, int value);

void system_out(DVM dvm, int c);

void load_program(DVM dvm, int *program_data, int length);

void dump_program(DVM dvm);

void cleanup_dvm(DVM dvm);

#endif
