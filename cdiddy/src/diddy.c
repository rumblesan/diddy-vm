#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <stdint.h>

#include "diddy.h"
#include "core/dvm.h"
#include "core/vmbase.h"

void usage(int exitval) {
    printf("Diddy usage:\n");
    printf("diddy input_file\n");
    exit(exitval);
}

Args parse_args(int argc, char *argv[]) {

    Args args = {""};

    int c;
    while ( (c = getopt(argc, argv, "h?")) != -1) {
        switch (c)
        {
            case '?':
            case 'h':
                usage(0);
                break;
        }
    }

    if (optind < argc) {
        args.input_file = argv[optind];
    }

    if (*args.input_file == '\0') {
        printf("Need to specify an input file\n");
        usage(1);
    } else {
        printf("Running %s\n", args.input_file);
    }

    return args;
}

int main(int argc, char *argv[]) {

	FILE *file;
	uint32_t *buffer;
	unsigned long fileLen;

    Args args = parse_args(argc, argv);

    printf("Opening file %s\n", args.input_file);

	//Open file
	file = fopen(args.input_file, "r");
	if (!file)
	{
		fprintf(stderr, "Unable to open file %s\n", args.input_file);
		return 1;
	}
	
	//Get file length
	fseek(file, 0, SEEK_END);
	fileLen = ftell(file) / 4;
	fseek(file, 0, SEEK_SET);

    fprintf(stdout, "File is %lu ints long\n", fileLen);

	//Allocate memory
	buffer = (uint32_t*) malloc(sizeof(uint32_t) * fileLen);
	if (!buffer)
	{
		fprintf(stderr, "Memory error!");
        fclose(file);
		return 1;
	}

	//Read file contents as ints into buffer
    int i;
    for (i = 0; i < fileLen; i++) {
        fread(&buffer[i], sizeof(uint32_t), 1, file);
    }

    DVM dvm = setup_diddy();
    load_program(dvm, buffer, fileLen);

	fclose(file);

    free(buffer);

    //dump_program(dvm);


    while (dvm->running == 1) {
        execute_next_instruction(dvm);
    }

    return 0;

}

