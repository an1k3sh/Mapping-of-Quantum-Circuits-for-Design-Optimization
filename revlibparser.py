from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Operator
from qiskit.circuit.library.standard_gates import SwapGate

# Defining the V and V+ (V-dagger) gates
v_gate = Operator([[(0.5+ 0.5j), (0.5 -0.5j)], [(0.5 -0.5j) , (0.5 +0.5j)]])
v_dagger_gate = Operator([[(0.5- 0.5j), (0.5+ 0.5j)], [(0.5+ 0.5j), (0.5 -0.5j)]])

# Function to find the names of registers used in an instruction
def registers_used(regs, instruction):
    used = []
    for command in instruction[1:]:
        for i in range(len(regs)):
            if command == regs[i].name:
                used.append(i)
    return used

# Function to parse the revlib benchmark
def read_circuit(file):
    
    file = open(file, "r")

    lines = file.readlines()

    i = 0

    while lines[i].find('.variables') == -1:
        i+=1
    
    # Defining the qubits (variables) in the circuit
    vars = lines[i].split()[1:]
    regs = []
    for j in vars:
        regs.append(QuantumRegister(1, j))

    while lines[i].find('.begin') == -1:
        i+=1
    i+=1

    qc = QuantumCircuit(*regs)

    # Parsing each instruction/gate
    while lines[i].find('.end') == -1:
        instruction = lines[i].split()
        if "t" == instruction[0][0]: # If the operation is a Toffoli gate
            n = int(instruction[0][1:])
            if n == 1:
                qc.x(*registers_used(regs, instruction))
            else:
                qc.mcx(control_qubits = registers_used(regs, instruction)[:-1], target_qubit = registers_used(regs, instruction)[-1])
        elif "f" == instruction[0][0]: # If the operation is a Fredkin gate
            n = int(instruction[0][1:])
            if n == 2:
                qc.swap(*registers_used(regs, instruction))
            else:
                cfredkin_gate = SwapGate().control(len(instruction[3:]))
                final_regs = [regs[i] for i in registers_used(regs, instruction)]
                qc.append(cfredkin_gate, final_regs)
        elif "p" == instruction[0][0]: # If the operation is a Peres gate
            for j in range(len(instruction[1:])-1, 0, -1) :
                qc.mcx(control_qubits = registers_used(regs, instruction)[0:j], target_qubit = registers_used(regs, instruction)[j])
        elif "v" == instruction[0]:  # If the operation is a Controlled-V gate
            circ = QuantumCircuit(1, name = "v")
            circ.unitary(v_gate, 0, label = "v")
            control_count = len(instruction[2:])
            cv_gate = circ.to_gate().control(control_count)
            final_regs = [regs[i] for i in registers_used(regs, instruction)]
            qc.append(cv_gate, final_regs)
        elif "v+" == instruction[0]: # If the operation is a Controlled-V+ gate
            circ = QuantumCircuit(1, name = "v_dg")
            circ.unitary(v_dagger_gate, 0, label = "v_dg")
            control_count = len(instruction[2:])
            cv_dagger_gate = circ.to_gate().control(control_count)
            final_regs = [regs[i] for i in registers_used(regs, instruction)]
            qc.append(cv_dagger_gate, final_regs)
        i+=1
    file.close()
    return qc