# Diddy VM

The Diddy VM is a project so I can learn more about writing virtual machines. It's not necessarily going to be the greatest piece of code ever but hopefully it should teach me a bunch of stuff.

The project is named after everybodies favorite rap star P Diddy.

![Diddy-VM](http://rumblesan.github.com/diddy-vm/img/diddy.jpg)

Little known fact **Diddy Loves Computer Science!**

## Aim

The plan is to build a simple VM in python that uses a minimal instruction set as an initial project. Eventually I'm aiming to have this VM rewritten in C and to build a basic compiler for a higher level language.

## Architecture

The Diddy VM has no registers and no stack so all operations happen entirely in memory. There aren't currently any memory constraints currently, the ram is just kept in a python list. The VM uses an positional counter to keep track of where the execution is currently happening.

The instructions all take up multiple memory entries, for example, the **Copy** instruction takes two arguments, where the data is being copied from and where it's being copied to. In memory this means that one memory slot is taken up by the jump instruction, the next by the source address and the next by the destination address.
It's not very efficient but it's simple to implement and makes things a bit more understandable I feel.

The VM program is split into two Python classes. VMBase sets up the RAM and the general machine methods such as setting/getting values in RAM and keeping track of the position counter. The DVM class inherits from the VMBase class and just contains the methods for the VM instructions.

There are fairly comprehensive unit tests for the two classes. To run them, cd to the dvm folder then run the class files. The test suits themselves are in the dvm/tests/ folder.

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
There is an assembler that will convert fairly low level machine code into the integer data that gets loaded into the VM memory. This can deal with labels to make addressing easier and will also substitute instruction names. As well as that it will strip out comments and white space so programs can be more easily written.
The example helloworld program is in the programs folder. This needs to be run through the assembler, which takes the path to the file as it's only argument. The assembled program is written out to the **compiled** folder.

## Running Programs
To run a program in the Diddy VM, use the diddy.py script and pass the path to the assembled program file as the only argument.

## Info
There is a suite of unit tests for the 

## Contact

guy@rumblesan.com if you have any questions

