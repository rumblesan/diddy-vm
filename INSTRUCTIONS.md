# Instructions

## Binary Format

All instructions are 32bit binary values

The 4 most significant bits specify the Instruction

The 5th and 6th most significant bits are the data and pointer flags.

The rest of the bits are for data that may be passed into the instruction.

## Flags

The data flag specifies if the data value for the instruction is passed in as part of the data bits or is pulled from the stack.

The pointer flag specifies if the data value is to be used directly or is a pointer to a position in memory

## Assembler

The assembler will compile the program written in Diddy VM Assembler into the binary byte code that the machine runs. Each line of assembler can have a few different parts.

### Label

A line can be denoted by a label. This is situated at the beginning of a line and must be a _lower case_ string, ending with a _:_. This label can be used elsewhere in the code and will be replaced with the line number of the label.

e.g.

1) start:    NOP
2)           start
3)           NOP

would be rewritten as :-

1) start:    NOP
2)           1
3)           NOP

### Instruction

Instructions need to be _upper case_. The assembler will calculate the correct byte code value for the instruction. Each instruction can also be specified with the data or pointer flags, though not all instructions will make use of them.

### Flags

The pointer flag needs to be specified before the data flag. The pointer flag is specified using a _*_, the data flag using a _#_.

e.g.

1)        *OUTPUT

This will pop the top value off the stack, use it as a pointer to a memory address, then print out the value found at that address.

1)        #JUMP    5

This will use the data value of 5 instead of popping the value off the stack
