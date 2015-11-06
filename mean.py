import sys
import numpy

length = len(sys.argv)
num_arguments = length - 1

if num_arguments >= 1:
    # print sys.argv
    for filename in sys.argv[1:]:
        if filename.startswith('inflammation'):
            data = numpy.loadtxt(filename, delimiter=',')
            print "mean inflammation value for",filename,":", data.mean()
        else:
            print "No mean calculated for non-inflammation file."
else:
    print "Excepted a command line argument"
    sys.exit(1)