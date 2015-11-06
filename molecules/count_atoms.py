import sys

def count_atom(filename, atom_type):
    """Count the number of a type of atom in a PDB file"""
    try:
        input_file = open(filename)
    except IOError as ex:
        print 'I got an error when opening', filename, ':', ex.strerror
        return None
    else:
        atom_count = 0
        for line in input_file:
            line = line.rstrip()
            if line.startswith('ATOM'):
                fields = line.split()
                if fields[2] == atom_type:
                    atom_count = atom_count + 1
        return atom_count

length = len(sys.argv)
num_arguments = length - 1
if num_arguments == 2:
    filename = sys.argv[1]
    atom_type = sys.argv[2]
    atom_count = count_atom(filename, atom_type)
    if atom_count is not None:
        print atom_count
else:
    print "Error: expected 2 command line arguments, got", num_arguments
    sys.exit(1)

