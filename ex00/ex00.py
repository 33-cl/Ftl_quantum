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
shots = 500
simulator = AerSimulator()
result = simulator.run(circuit, shots=shots).result()

# Convert counts to probabilities
counts = result.get_counts()
probabilities = {}
for state, count in counts.items():
    probabilities[state] = count / shots

# Display the results in a plot_histogram
plot_histogram(probabilities)
plt.ylabel("Probabilities")
plt.savefig("histogram.png")
plt.close()

