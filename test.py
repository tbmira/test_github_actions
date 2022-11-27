import os
absolute_path = os.path.dirname(__file__)
relative_path = "outFile.txt"
full_path = os.path.join(absolute_path, relative_path)

file = open(full_path, 'w')# ...

file.write("Olha eu aquiiii!") # ...
print("Done ;)")

f = open(full_path, 'r')
print((f.readline()))

file_2 = open(full_path.replace(".txt", "_2.txt", 'w'))
a = [1,
     2]
#.... 34234