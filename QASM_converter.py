from qiskit import qasm
import revlibparser

from os import listdir, makedirs
from os.path import isfile, join, exists

# Locating the benchmarks
# The benchmarks should be in a folder named real, which is present in the same directory as this converter and revlibparser
file_dir = '/'.join(__file__.split("/")[:-1])
dirpath = file_dir+"/reals"
realfiles = [fname for fname in listdir(dirpath) if isfile(join(dirpath, fname))]


# Create directory "qasm_files" to store the results
if not exists(file_dir+"/qasm_files/"):
   makedirs(file_dir+"/qasm_files/")

for fl in realfiles:
    qasm_file = open(file_dir+"/qasm_files/"+fl[:-5]+".qasm", "w")
    qc = revlibparser.read_circuit(dirpath+"/"+fl) # Parsing the .real benchmark into a Quantum Circuit
    qasm_file.write(qc.qasm()) # Writing QASM code of the Quantum Circuit into the QASM file
    qasm_file.close()