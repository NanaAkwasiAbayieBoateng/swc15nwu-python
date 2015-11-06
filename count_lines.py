import sys

num_arguments = len(sys.argv) - 1

filename = sys.argv[1]
try:
    input_file = open(filename)
except IOError as e:
    print "Unable to open", filename, ":", e.strerror
    sys.exit(1)
else:
    # count the number of lines in the file and
    # print out the result