import math
import warnings
warnings.filterwarnings(action='ignore', category=FutureWarning) # setting ignore as a parameter and further adding category
import revlibparser
import csv
# import copy
# from time import sleep

from os import listdir, makedirs
from os.path import isfile, join, exists

file_dir = '/'.join(__file__.split("/")[:-1])
dirpath = file_dir+"/reals"
readfiles = [fname for fname in listdir(dirpath) if isfile(join(dirpath, fname))]
realfiles = []
for i in readfiles:
   if i[-5:] == ".real":
      realfiles.append(i)
if not exists(file_dir+"/result_imp/"):
   makedirs(file_dir+"/result_imp/")

fields = ['Benchmark', 'Gate Count', 'Swap Count', 'Quantum Cost', 'Computer Name']

data = []

def Sort(List):
   List.sort(reverse = True, key=lambda l: l[3])
   return List

def make_grid_structure(qubit_count):
   if (qubit_count <= 5):
      lattice_size1 = lattice_size2 = 3
      grid_struct = [[None for i in range(lattice_size2)] for j in range(lattice_size1)]
      grid_struct[1][0] = 'X'
      grid_struct[2][0] = 'X'
      grid_struct[1][2] = 'X'
      grid_struct[2][2] = 'X'
      name = "IBM Quito"
   elif (qubit_count <= 7):
      lattice_size1 = lattice_size2 = 3
      grid_struct = [[None for i in range(lattice_size2)] for j in range(lattice_size1)]
      grid_struct[1][0] = 'X'
      grid_struct[1][2] = 'X'
      name = "IBM Nairobi"
   elif (qubit_count <= 16):
      grid_struct = [['X' , 'X' , 'X' , None, 'X' , 'X' , 'X' ],
                     [None, None, None, None, None, None, None],
                     ['X' , None, 'X' , 'X' , 'X' , None, 'X' ],
                     ['X' , None, None, None, None, None, 'X' ],
                     ['X' , 'X' , 'X' , None, 'X' , 'X' , 'X' ]]
      lattice_size1 = 5
      lattice_size2 = 7
      name = "IBM Guadeloupe"
   elif (qubit_count <= 27):
      grid_struct = [['X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' ],
                     [None, None, None, None, None, None, None, None, None, None, 'X' ],
                     ['X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' ],
                     ['X' , None, None, None, None, None, None, None, None, None, None],
                     ['X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' ]]
      lattice_size1 = 5
      lattice_size2 = 11
      name = "IBM Cairo"
   elif (qubit_count <=127):
      grid_struct = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'X' ],
                     [None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' ],
                     [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                     ['X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None],
                     [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                     [None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' ],
                     [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                     ['X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None],
                     [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                     [None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' ],
                     [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
                     ['X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None, 'X' , 'X' , 'X' , None],
                     ['X' , None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
      lattice_size1 = 13
      lattice_size2 = 15
      name = "IBM Sherbrooke"
   else:
      lattice_size1 = math.ceil(math.sqrt(qubit_count))
      lattice_size2 = math.ceil(qubit_count/lattice_size1)
      grid_struct =  [[None for j in range(lattice_size2)] for i in range(lattice_size1)]
      name = "Ideal Lattice"
   return grid_struct, lattice_size1, lattice_size2, name

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

def sum_par(i):
   return i[0]+i[1]

# def print_gs(grid_struct):
#    for i in range(len(grid_struct)):
#       for j in range(len(grid_struct[0])):
#          if grid_struct[i][j] is None:
#             print(' ', end=' ')
#          elif grid_struct[i][j] in ['X1', 'X2', 'X3', 'X4']:
#             print(grid_struct[i][j][0], end=' ')
#          else:
#             print(index[grid_struct[i][j]], end=' ')
#       print()

def print_gs(grid_struct, swap_result_file):
   for i in range(len(grid_struct)):
      for j in range(len(grid_struct[0])):
         if grid_struct[i][j] is None:
            swap_result_file.write(" \t")
            # print(' ', end=' ')
         elif grid_struct[i][j] == 'X':
            swap_result_file.write(grid_struct[i][j]+'\t')
         else:
            swap_result_file.write(str(index[grid_struct[i][j]])+"\t")
            # print(index[grid_struct[i][j]], end=' ')
      swap_result_file.write("\n")
      # print()
   swap_result_file.write("\n")



# print(realfiles)
# print(len(realfiles))


for fl in realfiles:
   # print(fl)
   
   qc = revlibparser.read_circuit(dirpath+"/"+fl)

   swap_result_file = open(file_dir+"/result_imp/"+fl[:-5]+"_swaps.txt", "w")

   # if (fl == '0410184_170.real'):
   #    continue

   index = {}
   ind = 0
   for i in qc.qubits:
      index[i] = ind
      ind += 1

   # for gate in qc.data:
   #    print('\ngate name:', gate[0].name)
   #    print('qubit(s) acted on:', gate[1])
   #    print('other paramters (such as angles):', gate[0].params)
   
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

   # if (len(pref_table)) > 16:
   #    continue
   grid_struct, lattice_size1, lattice_size2, Qname = make_grid_structure(len(pref_table))

   center_point = max_emp_neigh(grid_struct, lattice_size1, lattice_size2)
   center_point.sort(key = sum_par)

   count = 1
   prev=[None, None]
   for q_dat in sorted_pref_table:
      if count==1:
         grid_struct[center_point[int(len(center_point)/2)][0]][center_point[int(len(center_point)/2)][1]] = q_dat[0]
         prev[0] = center_point[int(len(center_point)/2)][0]
         prev[1] = center_point[int(len(center_point)/2)][1]
         count = count+1
      else:
         loc = max_emp_neigh(grid_struct, lattice_size1, lattice_size2)
         if len(loc) == 1:
            grid_struct[loc[0][0]][loc[0][1]] = q_dat[0]
            prev[0] = loc[0][0]
            prev[1] = loc[0][1]
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
   
   print_gs(grid_struct, swap_result_file)
   # print_gs(grid_struct)
   swap_count = 0
   # print()
   for gate in qc.data:
      if len(gate[1]) == 1:
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
         # print("no swap")
         print_gs(grid_struct, swap_result_file)
         # print_gs(grid_struct)
         # print()
         # print("Gate achieved: ",gate[0].name, index[gate[1][0]], index[gate[1][1]])
         # print()
      else:
         dx = l1_x - l2_x
         dy = l1_y - l2_y
         dirchange = ""
         while (math.fabs(dx) + math.fabs(dy) != 1):
            # print("GOAL", gate[0].name, index[gate[1][0]], index[gate[1][1]], dirchange)
            # print(dx, dy)
            if dx > 0 and grid_struct[l1_x - 1][l1_y] != 'X':
               grid_struct[l1_x - 1][l1_y], grid_struct[l1_x][l1_y] = grid_struct[l1_x][l1_y], grid_struct[l1_x - 1][l1_y]
               dict[grid_struct[l1_x - 1][l1_y]] = [l1_x - 1, l1_y]
               dict[grid_struct[l1_x][l1_y]] = [l1_x, l1_y]
            elif dx > 0 and grid_struct[l2_x + 1][l2_y] != 'X':
               grid_struct[l2_x + 1][l2_y], grid_struct[l2_x][l2_y] = grid_struct[l2_x][l2_y], grid_struct[l2_x + 1][l2_y]
               dict[grid_struct[l2_x + 1][l2_y]] = [l2_x + 1, l2_y]
               dict[grid_struct[l2_x][l2_y]] = [l2_x, l2_y]
            elif dx < 0 and grid_struct[l1_x + 1][l1_y] != 'X':
               grid_struct[l1_x + 1][l1_y], grid_struct[l1_x][l1_y] = grid_struct[l1_x][l1_y], grid_struct[l1_x + 1][l1_y]
               dict[grid_struct[l1_x + 1][l1_y]] = [l1_x + 1, l1_y]
               dict[grid_struct[l1_x][l1_y]] = [l1_x, l1_y]
            elif dx < 0 and grid_struct[l2_x - 1][l2_y] != 'X':
               grid_struct[l2_x - 1][l2_y], grid_struct[l2_x][l2_y] = grid_struct[l2_x][l2_y], grid_struct[l2_x - 1][l2_y]
               dict[grid_struct[l2_x - 1][l2_y]] = [l2_x - 1, l2_y]
               dict[grid_struct[l2_x][l2_y]] = [l2_x, l2_y]
            elif dy > 0 and grid_struct[l1_x][l1_y - 1] != 'X':
               grid_struct[l1_x][l1_y - 1], grid_struct[l1_x][l1_y] = grid_struct[l1_x][l1_y], grid_struct[l1_x][l1_y - 1]
               dict[grid_struct[l1_x][l1_y - 1]] = [l1_x, l1_y - 1]
               dict[grid_struct[l1_x][l1_y]] = [l1_x, l1_y]
            elif dy > 0 and grid_struct[l2_x][l2_y + 1] != 'X':
               grid_struct[l2_x][l2_y + 1], grid_struct[l2_x][l2_y] = grid_struct[l2_x][l2_y], grid_struct[l2_x][l2_y + 1]
               dict[grid_struct[l2_x][l2_y + 1]] = [l2_x, l2_y + 1]
               dict[grid_struct[l2_x][l2_y]] = [l2_x, l2_y]
            elif dy < 0 and grid_struct[l1_x][l1_y + 1] != 'X':
               grid_struct[l1_x][l1_y + 1], grid_struct[l1_x][l1_y] = grid_struct[l1_x][l1_y], grid_struct[l1_x][l1_y + 1]
               dict[grid_struct[l1_x][l1_y + 1]] = [l1_x, l1_y + 1]
               dict[grid_struct[l1_x][l1_y]] = [l1_x, l1_y]
            elif dy < 0 and grid_struct[l2_x][l2_y - 1] != 'X':
               grid_struct[l2_x][l2_y - 1], grid_struct[l2_x][l2_y] = grid_struct[l2_x][l2_y], grid_struct[l2_x][l2_y - 1]
               dict[grid_struct[l2_x][l2_y - 1]] = [l2_x, l2_y - 1]
               dict[grid_struct[l2_x][l2_y]] = [l2_x, l2_y]
            else:
               # sleep(1)
               if dx == 0 and 'X' in [grid_struct[l2_x][i] for i in range(l1_y, l2_y, -int(dy/math.fabs(dy)))]:
                  # print(111)
                  if dirchange!="-x" and (l1_x+1 < lattice_size1 and grid_struct[l1_x+1][l1_y] != 'X' and grid_struct[l2_x+1][l2_y] !='X'):
                     grid_struct[l1_x + 1][l1_y], grid_struct[l1_x][l1_y] = grid_struct[l1_x][l1_y], grid_struct[l1_x + 1][l1_y]
                     dict[grid_struct[l1_x + 1][l1_y]] = [l1_x + 1, l1_y]
                     dict[grid_struct[l1_x][l1_y]] = [l1_x, l1_y]
                     swap_result_file.write("swap\n")
                     print_gs(grid_struct, swap_result_file)
                     grid_struct[l2_x + 1][l2_y], grid_struct[l2_x][l2_y] = grid_struct[l2_x][l2_y], grid_struct[l2_x + 1][l2_y]
                     dict[grid_struct[l2_x + 1][l2_y]] = [l2_x + 1, l2_y]
                     dict[grid_struct[l2_x][l2_y]] = [l2_x, l2_y]
                     dirchange = "+x"
                  elif dirchange!="+x" and (l1_x-1 >= 0 and grid_struct[l1_x-1][l1_y] != 'X' and grid_struct[l2_x-1][l2_y] !='X'):
                     grid_struct[l1_x - 1][l1_y], grid_struct[l1_x][l1_y] = grid_struct[l1_x][l1_y], grid_struct[l1_x - 1][l1_y]
                     dict[grid_struct[l1_x - 1][l1_y]] = [l1_x - 1, l1_y]
                     dict[grid_struct[l1_x][l1_y]] = [l1_x, l1_y]
                     swap_result_file.write("swap\n")
                     print_gs(grid_struct, swap_result_file)
                     grid_struct[l2_x - 1][l2_y], grid_struct[l2_x][l2_y] = grid_struct[l2_x][l2_y], grid_struct[l2_x - 1][l2_y]
                     dict[grid_struct[l2_x - 1][l2_y]] = [l2_x - 1, l2_y]
                     dict[grid_struct[l2_x][l2_y]] = [l2_x, l2_y]
                     dirchange = "+x"
               elif dy == 0 and 'X' in [grid_struct[i][l2_y] for i in range(l1_x, l2_x, -int(dx/math.fabs(dx)))]:
                  # print(222)
                  if dirchange!="-y" and (l1_y+1 < lattice_size2 and grid_struct[l1_x][l1_y+1] != 'X' and grid_struct[l2_x][l2_y+1] !='X'):
                     # print(22211)
                     grid_struct[l1_x][l1_y + 1], grid_struct[l1_x][l1_y] = grid_struct[l1_x][l1_y], grid_struct[l1_x][l1_y + 1]
                     dict[grid_struct[l1_x][l1_y + 1]] = [l1_x, l1_y + 1]
                     dict[grid_struct[l1_x][l1_y]] = [l1_x, l1_y]
                     swap_result_file.write("swap\n")
                     print_gs(grid_struct, swap_result_file)
                     grid_struct[l2_x][l2_y + 1], grid_struct[l2_x][l2_y] = grid_struct[l2_x][l2_y], grid_struct[l2_x][l2_y + 1]
                     dict[grid_struct[l2_x][l2_y + 1]] = [l2_x, l2_y + 1]
                     dict[grid_struct[l2_x][l2_y]] = [l2_x, l2_y]
                     dirchange = "+y"
                  elif dirchange!="+y" and (l1_y-1 >= 0 and grid_struct[l1_x][l1_y-1] != 'X' and grid_struct[l2_x][l2_y-1] !='X'):
                     # print(22212)
                     grid_struct[l1_x][l1_y - 1], grid_struct[l1_x][l1_y] = grid_struct[l1_x][l1_y], grid_struct[l1_x][l1_y - 1]
                     dict[grid_struct[l1_x][l1_y - 1]] = [l1_x, l1_y - 1]
                     dict[grid_struct[l1_x][l1_y]] = [l1_x, l1_y]
                     swap_result_file.write("swap\n")
                     print_gs(grid_struct, swap_result_file)
                     grid_struct[l2_x][l2_y - 1], grid_struct[l2_x][l2_y] = grid_struct[l2_x][l2_y], grid_struct[l2_x][l2_y - 1]
                     dict[grid_struct[l2_x][l2_y - 1]] = [l2_x, l2_y - 1]
                     dict[grid_struct[l2_x][l2_y]] = [l2_x, l2_y]       
                     dirchange = "-y"
               # else:
                  # print(333)
                  # print(gate[0].name, index[gate[1][0]], index[gate[1][1]], dirchange)
                  # print(dx, dy)
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
   
   print(swap_count, len(qc.data))
   data.append([fl[:-5], len(qc.data), swap_count, len(qc.data)+swap_count, Qname])
   print(data[-1])
   swap_result_file.close()

overall_result_file = open(file_dir+"/swaps_imp.csv", "w")
csvwriter = csv.writer(overall_result_file)
csvwriter.writerow(fields)
csvwriter.writerows(data)