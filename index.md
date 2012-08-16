---
layout: page
---

# Diddy VM

## About

The Diddy VM is a project so I can learn more about writing virtual machines. It's not necessarily going to be the greatest piece of code ever but hopefully it should teach me a bunch of stuff.

The project is named after everybodies favorite rap star P Diddy. Little known fact, **Diddy Loves Computer Science!**

![Diddy-VM](http://rumblesan.github.com/diddy-vm/img/diddy.jpg)

## Aim

The Diddy VM is very simple and has implementations in Python and C called, respectively, P-Diddy and C-Diddy. (Honestly I didn't start this with that pun in mind, it just happened.)
There is a basic assembler to make writing code at such a low level a bit easier and I'm gradually creating a compiler for an as yet un-finalised language.

## Architecture

The Diddy VM has no registers and no stack so all operations happen entirely in memory. The memory size is arbitrarily 2^12 elements. In Python this uses a list so value size isn't an issue. In C this is an array of integers so a little bit more care must be taken. The VM uses an positional counter to keep track of where the execution is currently happening.

The instructions all take up multiple memory entries, for example, the **Copy** instruction takes two arguments, where the data is being copied from and where it's being copied to. In memory this means that one memory slot is taken up by the instruction, the next by the source address and the next by the destination address.
It's not very efficient but it's simple to implement and makes things a bit more understandable I feel.

The VM program is split into two sections. VMBase sets up the RAM and the general machine methods such as setting/getting values in RAM and keeping track of the position counter. The DVM class extends this and just contains the methods for the VM instructions.
In Python these are two separate classes. In C the VMBase is a struct and function library with the instructions being further functions that operate on it.

There are fairly comprehensive unit tests for the Python classes. To run them, cd to the dvm folder then run the class files. The test suits themselves are in the tests folder.
There aren't tests for the C yet, it's on the TODO list.

### Instructions

The VM has 11 instructions currently :-

* NOP
* Copy
* Jump
* Branch
* Equal
* Greater Than
* Less Than
* Add
* Subtract
* Output
* Halt

All arguments to instructions are actually addresses to other points in memory. It's probablly going to lead to some spaghetti code but it's consistant at least.

#### NOP
NOP takes no instructions and just increments the position counter.

#### Copy
Takes two argument, a source address **A** and a destination address **B**.
Copies the data from **A** to **B**.

#### Jump
Takes one argument, a source address **A**.
Sets the position counter to the value at **A**.

#### Branch
Takes three arguments, a source address **A** and two destination addresses, **B** and **C**.
If the value at **A** is not 0 then the position counter is set to address **B**, otherwise it's set to address **C**.

#### Equal
Takes three arguments, two source addresses **A** and **B** and two a destination address **C**.
If the values at **A** and **B** are equal then the memory position at address **C** is set to 1, otherwise it's set to 0.

#### Greater Than
Takes three arguments, two source addresses **A** and **B** and two a destination address **C**.
If the value at **A** is greater than **B** then the memory position at address **C** is set to 1, otherwise it's set to 0.

#### Less Than
Takes three arguments, two source addresses **A** and **B** and a destination address **C**.
If the value at **A** is less than **B** then the memory position at address **C** is set to 1, otherwise it's set to 0.

#### Add
Takes three arguments, two source addresses **A** and **B** and a destination address **C**.
Adds the value at **A** to the value at **B** and writes the result to **C**.

#### Subtract
Takes three arguments, two source addresses **A** and **B** and a destination address **C**.
Subtracts the value at **B** from the value at **A** and writes the result to **C**.

#### Output
Takes one argument, a source address **A**.
Writes the value at **A** to the screen, the number is converted into an ascii character.

#### Halt
Takes one argument, a source address **A**.
Stops the VM and sets the status to the value at address **A**.

## Writing Programs
There is an assembler that will convert fairly low level machine code into the binary integer data that gets loaded into the VM memory. This can deal with labels to make addressing easier and will also substitute instruction names. As well as that it will strip out comments and white space so programs can be more easily written.
The example helloworld program is in the programs folder. This needs to be run through the assembler, which takes the path to the file as it's only argument. The assembled program is written out to the **compiled** folder.

## Running Programs
To run a program in the P-Diddy VM, use the diddy.py script and pass the path to the assembled program file as the only argument. To run it on C-Diddy you need to first compile it. Once that's done, call the cdiddy executable that's been created and pass in the compiled program name as an argument.

## Future
There are a few things I want to do with the base VM in future, other than fix all the small niggly problems.
* Have single element instructions
* Rely less on spaghetti "everything a pointer" style
* Add the ability to have some user input loaded

## Info
There is a suite of unit tests for the VM which are fairly comprehensive. If you want to contribute, make sure they all stay running.

## Contact
guy@rumblesan.com if you have any questions

