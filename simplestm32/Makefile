
CFLAGS =-g -O0
CFLAGS += "-I/pb"

# C source code files that are required
CSRC  = main.c                   # The main program
CSRC += simplestm32.pb.c                # The compiled protocol definition
CSRC += pb/pb_encode.c  # The nanopb encoder
CSRC += pb/pb_decode.c  # The nanopb decoder
CSRC += pb/pb_common.c  # The nanopb common parts

main.exe: $(CSRC)
	$(CC) $(CFLAGS) -omain $(CSRC)
