from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Creating superposition
circuit = QuantumCircuit(1)
circuit.h(0)
circuit.measure_all()

# Launching simulation 500 times
simulator = AerSimulator()
result = simulator.run(circuit, shots=500).result()
counts = result.get_counts()

# Creating a graph for the experience and saving it
graph = plot_histogram(counts)
graph.savefig("superposition.png")

