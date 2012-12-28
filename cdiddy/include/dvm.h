#ifndef DVM_H
#define DVM_H

#include <stdint.h>

#include "vmbase.h"

DVM setup_diddy();

void nop(DVM dvm, uint32_t data);

void push(DVM dvm, uint32_t data);

void pop(DVM dvm, uint32_t data);

void jump(DVM dvm, uint32_t data);

void branch(DVM dvm, uint32_t data);

void equal(DVM dvm, uint32_t data);

void greater(DVM dvm, uint32_t data);

void lesser(DVM dvm, uint32_t data);

void add(DVM dvm, uint32_t data);

void subtract(DVM dvm, uint32_t data);

void output(DVM dvm, uint32_t data);

void halt(DVM dvm, uint32_t data);

#endif
