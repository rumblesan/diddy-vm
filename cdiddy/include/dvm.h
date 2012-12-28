#ifndef DVM_H
#define DVM_H

#include <stdint.h>

#include "vmbase.h"

DVM setup_diddy();

void nop(DVM dvm, uint32_t bits);

void push(DVM dvm, uint32_t bits);

void pop(DVM dvm, uint32_t bits);

void jump(DVM dvm, uint32_t bits);

void branch(DVM dvm, uint32_t bits);

void equal(DVM dvm, uint32_t bits);

void greater(DVM dvm, uint32_t bits);

void lesser(DVM dvm, uint32_t bits);

void add(DVM dvm, uint32_t bits);

void subtract(DVM dvm, uint32_t bits);

void output(DVM dvm, uint32_t bits);

void halt(DVM dvm, uint32_t bits);

#endif
