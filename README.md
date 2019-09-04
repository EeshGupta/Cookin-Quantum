# Cookin-Quantum

Cookin-Quantum is an open source framework for simulating quantum programs. The goal of this project is to simulate and optimize important Quantum algorithms in fields of encryption and machine learning.

## Installation

This project is to be run on an ipython IDE. I reccomend downloading anaconda from https://www.anaconda.com/distribution/, forking and downloading this repository, and running this project on Spyder.

## Usage

Here we apply the Hadamard Gate to the first qubit in 2 qubit Quantum Circuit and see how such operation affects the probability amplitudes of basis states.

Run the QuantumCircuit file from cookin-quantum/circuit
```python
qc = QuantumCircuit(2)
qc.gates.Hadamard(0)
qc.register.state_vector
```

Output:
```python
{'00': 0.7071067811865475, '01': 0.0, '10': 0.7071067811865475, '11': 0.0}
```

## Architecture
The main class in QuantumCircuit which is used to generate quantum programs. Classes built into the QuantumCircuit include register (controls state vector operations) and gates (controls various operations to be performed on the quantum circuit). Finally Quantum Circuit class has a measure method, which can simulate measured results of a quantum computation. 

Besides the simulator, there is a folder which includes simulation of Grover and Shor's algorithms. Along with these simulations are loosely related number theory projects, constructed to understand the parts of Shor's algorithm.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## Contact
For more information/suggestions regarding this project and quantum computing in general, please contact me at my email: eesh.gupta@rutgers.edu

## References
The main architecture of the cookin-quantum framework was built with the help of Don Candela's research paper ["Undergraduate computational physics projects on quantum computing"](https://www.semanticscholar.org/paper/Undergraduate-computational-physics-projects-on-Candela/a1234106949ad338bf668853ee48199b08b2e4ce) .

## License
[MIT](https://choosealicense.com/licenses/mit/)
