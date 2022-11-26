import os


absolute_path = os.path.dirname(__file__)
relative_path = 'outFile.txt'
full_path = os.path.join(absolute_path, relative_path)

file = open(full_path, 'w')

file.write('Olha eu aquiiii!')
print('Done ;)')
