# Cookin-Quantum

Cookin-Quantum is an open source framework for simulating quantum programs. The goal of this project is to simulate and optimize important Quantum algorithms in fields of encryption and machine learning.

## Installation

This project is to be run on an ipython IDE. I reccomend downloading anaconda from https://www.anaconda.com/distribution/, forking and downloading this repository, and running this project on Spyder.

## Usage

Here we apply the Hadamard Gate to the first qubit and see how such operation affects the probability amplitudes of basis states.

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
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## References
The main architecture of the cookin-quantum framework was built with the help of Don Candela's research paper "Undergraduate computational physics projects on quantum computing" which can be found here: https://www.semanticscholar.org/paper/Undergraduate-computational-physics-projects-on-Candela/a1234106949ad338bf668853ee48199b08b2e4ce


## License
[MIT](https://choosealicense.com/licenses/mit/)
