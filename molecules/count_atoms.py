def count_atom(filename, atom_type):
    try:
        input_file = open(filename)
    except IOError as ex:
        print 'I got an error when opening', filename, ':', ex.strerror
    else:
        atom_count = 0
        for line in input_file:
            line = line.rstrip()
            if line.startswith('ATOM'):
                fields = line.split()
                if fields[2] == atom_type:
                    atom_count = atom_count + 1
    return atom_count

print count_atom('methane.pdb', 'H')
