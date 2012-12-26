# Instructions

## Binary Format

All instructions are 32bit binary values

The 4 most significant bits specify the Instruction

The 5th and 6th most significant bits are the stack and pointer flags.

The rest of the bits are for data that may be passed into the instruction.

## Flags

The stack flag specifies if the data value for the instruction is passed in as part of the data bits or is pulled from the stack.

The pointer flag specifies if the data value is to be used directly or is a pointer to a position in memory

