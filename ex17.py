from sys import argv
from os.path import exists

script, from_flie, to_file = argv

print(f"Coping from {from_flie} to {to_file}")

indata = open(from_flie).read()
print(f"The input file is {len(indata)} bytes long.")
print(f"Does the output file exists?{exists(to_file)}")
#maybe you should care about the {}

print("Ready, hit RETURN to coutinue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("All right, all done.")

out_file.close()
