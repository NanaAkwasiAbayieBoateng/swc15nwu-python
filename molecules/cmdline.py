import sys

print sys.argv

length = len(sys.argv)
num_arguments = length - 1
if num_arguments == 1:
  print "Hello", sys.argv[1]

