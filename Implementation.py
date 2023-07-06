#from qiskit import QuantumCircuit
import math
import warnings
warnings.filterwarnings(action='ignore', category=FutureWarning) # setting ignore as a parameter and further adding category
import revlibparser
import copy
import csv

from os import listdir, makedirs
from os.path import isfile, join, exists

file_dir = '/'.join(__file__.split("/")[:-1])
dirpath = file_dir+"/reals"
realfiles = [fname for fname in listdir(dirpath) if isfile(join(dirpath, fname))]

if not exists(file_dir+"/result/"):
   makedirs(file_dir+"/result/")

fields = ['Benchmark', 'Gate Count', 'Swap Count', 'Quantum Cost']

data = []

# def print_gs(grid_struct):
#     for i in range(len(grid_struct)):
#         for j in range(len(grid_struct[0])):
#             if grid_struct[i][j] is None:
#                 print(' ', end=' ')
#             else:
#                 print(index[grid_struct[i][j]], end=' ')
#         print()

def print_gs(grid_struct, swap_result_file):
    for i in range(len(grid_struct)):
        for j in range(len(grid_struct[0])):
            if grid_struct[i][j] is None:
                swap_result_file.write("  ")
                # print(' ', end=' ')
            else:
                swap_result_file.write(str(index[grid_struct[i][j]])+" ")
                # print(index[grid_struct[i][j]], end=' ')
        swap_result_file.write("\n")
        # print()
    swap_result_file.write("\n")


def Sort(List):
    List.sort(reverse = True, key=lambda l: l[3])
    return List

def count_emp_neigh(grid_struct, i, j, M, N):
    count = 0
    if i>0 and grid_struct[i-1][j] is None:
        count = count+1
    if j>0 and grid_struct[i][j-1] is None:
        count = count+1
    if i<M-1 and grid_struct[i+1][j] is None:
        count = count+1
    if j<N-1 and grid_struct[i][j+1] is None:
        count = count+1
    return count

def max_emp_neigh(grid_struct, M, N):
    max = 0
    loc = [[]]
    for i in range(M):
        for j in range(N):
            if count_emp_neigh(grid_struct, i, j, M, N) > max and grid_struct[i][j] is None:
                max = count_emp_neigh(grid_struct, i, j, M, N)
                loc=[[i,j]]
            elif count_emp_neigh(grid_struct, i, j, M, N) == max and grid_struct[i][j] is None:
                loc.append([i,j])
    return loc

for fl in realfiles:
    qc = revlibparser.read_circuit(dirpath+"/"+fl)

    swap_result_file = open(file_dir+"/result/"+fl[:-5]+"_swaps.txt", "w")

    index = {}
    ind = 0
    for i in qc.qubits:
        index[i] = ind
        ind += 1
    
    # for gate in qc.data:
    #     print('\ngate name:', gate[0].name)
    #     print('qubit(s) acted on:', gate[1])
    #     print('other paramters (such as angles):', gate[0].params)

    costing = [[None for i in range(5)] for j in range(len(qc.qubits))]

    for i in range(len(qc.qubits)):
        costing[i][0] = qc.qubits[i]
        costing[i][1] = []
        costing[i][3] = []
    
    time = 0
    for gate in qc.data:
        if len(gate[1]) == 1:
            continue
        time = time+1
        costing[index[gate[1][0]]][1].append(time)
        costing[index[gate[1][1]]][1].append(time)
        if math.fabs(index[gate[1][0]]-index[gate[1][1]])!=1:
            costing[index[gate[1][0]]][3].append(time)
            costing[index[gate[1][1]]][3].append(time)

    for i in range(len(qc.qubits)):
        costing[i][2] = sum(costing[i][1])
        costing[i][4] = sum(costing[i][3])

    pref_table =[]
    for i in costing:
        pref_table.append([])
        pref_table[-1].extend([i[0],i[2],i[4],i[4]/i[2]])
    

    sorted_pref_table = Sort(pref_table)

    lattice_size1 = lattice_size2 = math.ceil(math.sqrt(len(index)))

    grid_struct = [[None for i in range(lattice_size2)] for j in range(lattice_size1)]
    
    count = 1
    prev=[None, None]
    for q_dat in sorted_pref_table:
        if count==1:
            grid_struct[int(len(grid_struct)/2)][int(len(grid_struct[0])/2)] = q_dat[0]
            prev[0] = int(len(grid_struct)/2)
            prev[1] = int(len(grid_struct[0])/2)
            count = count+1
        else:
            i, j = prev
            assigned = False
            for a in [-1, 1, -2, 2]:
                if 0<=j+a<=lattice_size2-1 and grid_struct[i][j+a] is None:
                    grid_struct[i][j+a] = q_dat[0]
                    assigned = True
                    break
                if 0<=i+a<=lattice_size1-1 and grid_struct[i+a][j] is None:
                    grid_struct[i+a][j] = q_dat[0]
                    assigned = True
                    break
            if not assigned:    
                for a in range(0, lattice_size1):
                    for b in range(0, lattice_size2):
                        if 0<=i+a<=lattice_size1-1 and 0<=j+b<=lattice_size2-1 and grid_struct[i+a][j+b] is None:
                            grid_struct[i+a][j+b] = q_dat[0]
                            assigned = True
                            break
                        if 0<=i+a<=lattice_size1-1 and 0<=j-b<=lattice_size2-1 and grid_struct[i+a][j-b] is None:
                            grid_struct[i+a][j-b] = q_dat[0]
                            assigned = True
                            break
                        if 0<=i-a<=lattice_size1-1 and 0<=j+b<=lattice_size2-1 and grid_struct[i-a][j+b] is None:
                            grid_struct[i-a][j+b] = q_dat[0]
                            assigned = True
                            break
                        if 0<=i-a<=lattice_size1-1 and 0<=j-b<=lattice_size2-1 and grid_struct[i-a][j-b] is None:
                            grid_struct[i-a][j-b] = q_dat[0]
                            assigned = True
                            break
                    if (assigned):
                        break
    
    # intial_grid_struct = copy.deepcopy(grid_struct)

    dict = {}
    for i in range(lattice_size1):
        for j in range(lattice_size2):
            if grid_struct[i][j] is not None:
                dict[grid_struct[i][j]] = [i, j]
    
    #optimized_qc = QuantumCircuit(qc.num_qubits)

    print_gs(grid_struct, swap_result_file)
    # print_gs(grid_struct)
    swap_count = 0
    # print()
    for gate in qc.data:
        if len(gate[1]) == 1:
            swap_result_file.write("no swap\n")
            # print("no swap")
            print_gs(grid_struct, swap_result_file)
            # print_gs(grid_struct)
            # print()
            # print("Gate achieved: ",gate[0].name, index[gate[1][0]])
            # print()
            continue
        l1_x, l1_y = dict[gate[1][0]]
        l2_x, l2_y = dict[gate[1][1]]
    
        if ((l1_x == l2_x) and (math.fabs(l1_y - l2_y) == 1)) or ((l1_y == l2_y) and (math.fabs(l1_x - l2_x) == 1)):
            swap_result_file.write("no swap\n")
            # print("no swap")
            print_gs(grid_struct, swap_result_file)
            # print_gs(grid_struct)
            # print()
            # print("Gate achieved: ",gate[0].name, index[gate[1][0]], index[gate[1][1]])
            # print()
        else:
            dx = l1_x - l2_x
            dy = l1_y - l2_y
            while (math.fabs(dx) + math.fabs(dy) != 1):
                if dx > 0 and grid_struct[l1_x - 1][l1_y] is not None:
                    grid_struct[l1_x - 1][l1_y], grid_struct[l1_x][l1_y] = grid_struct[l1_x][l1_y], grid_struct[l1_x - 1][l1_y]
                    dict[grid_struct[l1_x - 1][l1_y]] = [l1_x - 1, l1_y]
                    dict[grid_struct[l1_x][l1_y]] = [l1_x, l1_y]
                elif dx > 0 and  grid_struct[l2_x + 1][l2_y] is not None:
                    grid_struct[l2_x + 1][l2_y], grid_struct[l2_x][l2_y] = grid_struct[l2_x][l2_y], grid_struct[l2_x + 1][l2_y]
                    dict[grid_struct[l2_x + 1][l2_y]] = [l2_x + 1, l2_y]
                    dict[grid_struct[l2_x][l2_y]] = [l2_x, l2_y]
                elif dx < 0 and grid_struct[l1_x + 1][l1_y] is not None:
                    grid_struct[l1_x + 1][l1_y], grid_struct[l1_x][l1_y] = grid_struct[l1_x][l1_y], grid_struct[l1_x + 1][l1_y]
                    dict[grid_struct[l1_x + 1][l1_y]] = [l1_x + 1, l1_y]
                    dict[grid_struct[l1_x][l1_y]] = [l1_x, l1_y]
                elif dx < 0 and  grid_struct[l2_x - 1][l2_y] is not None:
                    grid_struct[l2_x - 1][l2_y], grid_struct[l2_x][l2_y] = grid_struct[l2_x][l2_y], grid_struct[l2_x - 1][l2_y]
                    dict[grid_struct[l2_x - 1][l2_y]] = [l2_x - 1, l2_y]
                    dict[grid_struct[l2_x][l2_y]] = [l2_x, l2_y]
                elif dy > 0 and grid_struct[l1_x][l1_y - 1] is not None:
                    grid_struct[l1_x][l1_y - 1], grid_struct[l1_x][l1_y] = grid_struct[l1_x][l1_y], grid_struct[l1_x][l1_y - 1]
                    dict[grid_struct[l1_x][l1_y - 1]] = [l1_x, l1_y - 1]
                    dict[grid_struct[l1_x][l1_y]] = [l1_x, l1_y]
                elif dy > 0 and  grid_struct[l2_x][l2_y + 1] is not None:
                    grid_struct[l2_x][l2_y + 1], grid_struct[l2_x][l2_y] = grid_struct[l2_x][l2_y], grid_struct[l2_x][l2_y + 1]
                    dict[grid_struct[l2_x][l2_y + 1]] = [l2_x, l2_y + 1]
                    dict[grid_struct[l2_x][l2_y]] = [l2_x, l2_y]
                elif dy < 0 and grid_struct[l1_x][l1_y + 1] is not None:
                    grid_struct[l1_x][l1_y + 1], grid_struct[l1_x][l1_y] = grid_struct[l1_x][l1_y], grid_struct[l1_x][l1_y + 1]
                    dict[grid_struct[l1_x][l1_y + 1]] = [l1_x, l1_y + 1]
                    dict[grid_struct[l1_x][l1_y]] = [l1_x, l1_y]
                elif dy < 0 and  grid_struct[l2_x][l2_y - 1] is not None:
                    grid_struct[l2_x][l2_y - 1], grid_struct[l2_x][l2_y] = grid_struct[l2_x][l2_y], grid_struct[l2_x][l2_y - 1]
                    dict[grid_struct[l2_x][l2_y - 1]] = [l2_x, l2_y - 1]
                    dict[grid_struct[l2_x][l2_y]] = [l2_x, l2_y]
                l1_x, l1_y = dict[gate[1][0]]
                l2_x, l2_y = dict[gate[1][1]]
                dx = l1_x - l2_x
                dy = l1_y - l2_y
                swap_result_file.write("swap\n")
                # print("swap")
                swap_count += 1
                print_gs(grid_struct, swap_result_file)
                # print_gs(grid_struct)
                # print()
            # print("Gate achieved: ",gate[0].name, index[gate[1][0]], index[gate[1][1]])
            # print()

    print(swap_count, len(qc.data))
    data.append([fl[:-5], len(qc.data), swap_count, len(qc.data)+swap_count])
    print(data[-1])
    swap_result_file.close()

overall_result_file = open(file_dir+"/swaps.csv", "w")
csvwriter = csv.writer(overall_result_file)
csvwriter.writerow(fields)
csvwriter.writerows(data)