# Diddy VM

## About

The Diddy VM is a project so I can learn more about writing virtual machines. It's not necessarily going to be the greatest piece of code ever but hopefully it should teach me a bunch of stuff.

The project is named after everybodies favorite rap star P Diddy. Little known fact, **Diddy Loves Computer Science!**

![Diddy-VM](http://rumblesan.github.com/diddy-vm/img/diddy.jpg)

## Aim

The Diddy VM is very simple and has implementations in Python and C called, respectively, P-Diddy and C-Diddy. (Honestly I didn't start this with that pun in mind, it just happened.)
There is a basic assembler to make writing code at such a low level a bit easier and I'm gradually creating a compiler for an as yet un-finalised language.

## Architecture

The Diddy VM is stack based. The memory size is arbitrarily 2^12 elements. In Python this uses a list so value size isn't an issue. In C this is an array of unsigned, 32bit integers so a little bit more care must be taken. The VM uses an positional counter to keep track of where the execution is currently happening.

Each instruction uses the 4 most significant bits to specify what the instruction is, the next 2 bits for flags, and the rest of the bits as an optional data part that most of the instructions can make use of if the correct flag is set.
Further details can be found in the INSTRUCTIONS.md file.

The VM program is split into two sections. VMBase sets up the RAM, the Stack and the general machine methods such as setting/getting values in RAM and keeping track of the position counter. The DVM class extends this and just contains the methods for the VM instructions.
In Python these are two separate classes. In C the VMBase is a struct and function library with the instructions being further functions that operate on it.

There are fairly comprehensive testing suites for the Python and C code. To run the python tests, cd to the dvm folder then run the class files. The test suits themselves are in the tests folder.
To run the tests for the C code, cd to the cdiddy flder and run *make tests*. This will compile the code and run the tests, outputting the results. The C testing framework could be improved but it's fairly functional for the moment.

### Instructions

The VM has 12 instructions currently :-

* NOP
* Push
* Pop
* Jump
* Branch
* Equal
* Greater Than
* Less Than
* Add
* Subtract
* Output
* Halt

Most of these instructions can use the data or pointer flags.

#### NOP
NOP takes no instructions and just increments the position counter.

#### Push
Push a value onto the stack.

#### Pop
Pop the top value on the stack to a location in memory.

#### Jump
Set the instruction pointer to a specific memory position.

#### Branch
Jumps to the desired position in memory if the top stack value is not zero.

#### Equal
Check if the two values on top of the stack are equal. If they are then push a 1 onto the stack, otherwise push a 0.

#### Greater Than
Check if the top value on the stack is greater than the next from top. If they are then push a 1 onto the stack, otherwise push a 0.

#### Less Than
Check if the top value on the stack is lesser than the next from top. If they are then push a 1 onto the stack, otherwise push a 0.

#### Add
Add the top two values on the stack, then push the result.

#### Subtract
Subtract the top two values on the stack, then push the result.

#### Output
Write out a character.

#### Halt
Stops the VM and set the status.

## Writing Programs
There is an assembler that will convert fairly low level machine code into the binary data that gets loaded into the VM memory. This can deal with labels to make addressing easier, substitute instruction names and set data and pointer flags. As well as that it will strip out comments and white space so programs can be more easily written.
There are some example helloworld programs is in the programs folder. This needs to be run through the assembler, which takes the path to the file as it's only argument. The assembled program is written out to the **compiled** folder.

## Running Programs
To run a program in the P-Diddy VM, use the diddy.py script and pass the path to the assembled program file as the only argument. To run it on C-Diddy you need to first compile it. Once that's done, call the cdiddy executable that's been created and pass in the compiled program name as an argument.

## Debugging
The python implementation has a basic debugging console. This allows stepping through the program one instruction at a time as well as viewing the stack and memory contents.

## Future
There are a few things I want to do with the base VM in future, other than fix all the small niggly problems.
* Add the ability to have some user input loaded
* Improve the debugging console in PDidddy implementation

## Info
There is a suite of unit tests for the VM which are fairly comprehensive. If you want to contribute, make sure they all stay running.

## Contact
guy@rumblesan.com if you have any questions

