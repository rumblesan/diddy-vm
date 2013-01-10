CC                = clang
CFLAGS            = -Wall
LDFLAGS           = -c
VPATH             = src src/core src/tests
TEMP_DIR          = temp
HEADERS           = include/

CORE_SOURCES      = $(notdir $(wildcard src/core/*.c))
TEST_SOURCES      = $(notdir $(wildcard src/tests/*.c)) $(CORE_SOURCES)
DVM_SOURCES       = diddy.c $(CORE_SOURCES)

DVM_OBJECTS       = $(addprefix $(TEMP_DIR)/, $(DVM_SOURCES:.c=.o))
TEST_OBJECTS      = $(addprefix $(TEMP_DIR)/, $(TEST_SOURCES:.c=.o))

EXECUTABLE        = cdiddy
TEST_EXECUTABLE   = $(addprefix $(TEMP_DIR)/, test_cdiddy)

all: $(EXECUTABLE)

tests: $(TEST_EXECUTABLE)
	./$(TEST_EXECUTABLE)

$(TEMP_DIR)/%.o: %.c
	$(CC) $(LDFLAGS) $(CFLAGS) -I$(HEADERS) $< -o $@

$(EXECUTABLE): $(DVM_OBJECTS)
	$(CC) $(CFLAGS) $(DVM_OBJECTS) -o $@

$(TEST_EXECUTABLE): $(TEST_OBJECTS)
	$(CC) $(CFLAGS) $(TEST_OBJECTS) -o $@

clean:
	rm -rf $(TEMP_DIR)/*.o $(EXECUTABLE)

