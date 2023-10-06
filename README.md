
A Python program designed to simulate memory allocation for a set of jobs and the transfer of fragmented files into memory. 
## Project Description

The Memory Allocation and Fragmentation Simulator is a Python program designed to simulate memory allocation for a set of jobs and the transfer of fragmented files into memory. This project helps users explore memory management concepts, including allocation and the storage of fragmented files within a single file.

## Features

### Memory Allocation Simulation

The program simulates memory allocation for multiple jobs based on their start times, execution intervals, and memory requirements.

### File Fragmentation Simulation

The project includes a file fragmentation simulation in which fragmented file blocks are transferred into memory at specific intervals.

### Allocation Diagnosis

It offers a diagnostic node function to identify memory allocation failures and provides feedback if any allocation fails.

## Usage

1. Clone this repository to your local machine.

2. Run the `main.py` script to execute the memory allocation and fragmentation simulation.

3. View the allocation results and diagnostic messages in the console.

## Example Use Case

**Total Memory size**: 20 Kbyte
**Page size**: 1 Kbyte

**Initial memory**

| Memory Block | Size (KB) |
|--------------|-----------|
| 1            | 20        |

**Job Information**

| Job ID | Start Time | Job Required Size (KB) | Execution Interval | Job State at the End of the Interval |
|--------|------------|------------------------|--------------------|-------------------------------------|
| 1      | 1          | 2                      | 7                  | Sleep                               |
| 2      | 2          | 3                      | 8                  | Sleep                               |
| 3      | 3          | 4                      | 6                  | Sleep                               |
| 4      | 4          | 3                      | 6                  | Sleep                               |
| 5      | 5          | 2                      | 9                  | Sleep                               |
| 6      | 6          | 3                      | 6                  | Sleep                               |
| 7      | 7          | 2                      | 6                  | Sleep                               |

**File Information**

- File Size: 8 KB
- Disk Block Size: 1 KB
- Initial Disk Blocks: 28, 5, 12, 13, 1, 4
- File Stays in Memory Up to Interval 16
- File Needs to Be Transferred to Memory at Interval 12

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the contributors and developers who have helped make this project possible.
