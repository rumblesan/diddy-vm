#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#include "diddy.h"

void usage(int exitval) {
    printf("Diddy usage:\n");
    printf("diddy -i input_file\n");
    exit(exitval);
}

Args parse_args(int argc, char *argv[]) {

    Args args = {""};

    int c;
    while ( (c = getopt(argc, argv, "i:h")) != -1) {
        switch (c)
        {
            case 'i':
                args.input_file = optarg;
                break;
            case 'h':
                usage(0);
                break;
        }
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
	int *buffer;
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
	fileLen = ftell(file);
	fseek(file, 0, SEEK_SET);

    fprintf(stdout, "File is %lu bytes long\n", fileLen);

	//Allocate memory
	buffer = (int*) malloc(sizeof(int) * fileLen);
	if (!buffer)
	{
		fprintf(stderr, "Memory error!");
        fclose(file);
		return 1;
	}

	//Read file contents into buffer
	fread(buffer, fileLen, 1, file);
	fclose(file);

    int i;

    for(i = 0; i < fileLen; i++) {
        printf("%c", ((char *)buffer)[i]);
    }


    free(buffer);

    return 0;

}

