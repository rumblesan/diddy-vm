CC         = clang
CFLAGS     = -c -Wall
VPATH      = src
OBJDIR     = temp
SOURCES    = diddy.c dvm.c vmbase.c
OBJECTS    = $(addprefix $(OBJDIR)/, $(SOURCES:.c=.o))
HEADERS    = include/
EXECUTABLE = cdiddy

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@

$(OBJDIR)/%.o: %.c
	$(CC) $(CFLAGS) -I$(HEADERS) $< -o $@

clean:
	rm -rf $(OBJDIR)/*.o $(EXECUTABLE)

