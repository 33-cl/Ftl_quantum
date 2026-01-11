from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Creating superposition
circuit = QuantumCircuit(1)
circuit.h(0)
circuit.measure_all()

# Display the circuit
print(circuit.draw())

# Launching simulation 500 times
simulator = AerSimulator()
result = simulator.run(circuit, shots=500).result()
counts = result.get_counts()

# Display the results in a plot_histogram
plot_histogram(counts)
plt.savefig("superposition.png")
plt.close()

