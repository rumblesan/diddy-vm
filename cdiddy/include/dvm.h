#ifndef DVM_H
#define DVM_H

#include "vmbase.h"

DVM setup_diddy();

void nop(DVM dvm);

void copy(DVM dvm);

void jump(DVM dvm);

void branch(DVM dvm);

void equal(DVM dvm);

void greater(DVM dvm);

void lesser(DVM dvm);

void add(DVM dvm);

void subtract(DVM dvm);

void output(DVM dvm);

void halt(DVM dvm);

#endif
