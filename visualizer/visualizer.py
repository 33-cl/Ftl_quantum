from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# Creating a circuit with 1 qubit
circuit = QuantumCircuit(1)
first = 1

while 1:

    # Saving initial state
    if first:
        state = Statevector.from_instruction(circuit)
        plot_bloch_multivector(state)
        plt.savefig("visualizer.png")
        plt.close()
        first = 0


    # User applies a function to the qubit
    user_input = input("Enter a command : ")
    if user_input.lower() == "h":
        circuit.h(0)
    elif user_input.lower() == "x":
        circuit.x(0)
    else:
        print(f"{user_input}: invalid command")
        continue

    # Saving state after the function
    state = Statevector.from_instruction(circuit)
    plot_bloch_multivector(state)
    plt.savefig("visualizer.png")
    plt.close()
