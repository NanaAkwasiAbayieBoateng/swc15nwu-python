import sys

num_arguments = len(sys.argv) - 1

if num_arguments != 1:
    print "Expected a filename argument"
    sys.exit(1)

filename = sys.argv[1]
try:
    input_file = open(filename)
except IOError as e:
    print "Unable to open", filename, ":", e.strerror
    sys.exit(1)
else:
    # count the number of lines in the file and
    # print out the result
    count = 0
    for line in input_file:
        count = count + 1
    print count