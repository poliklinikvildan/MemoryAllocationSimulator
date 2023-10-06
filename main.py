class MemoryManager:
    def __init__(self, total_memory_size_kb):
        self.total_memory_size_kb = total_memory_size_kb
        self.fragments = [total_memory_size_kb]  # Initialize with the total memory size

    def allocate(self, job_size):
        for i, fragment in enumerate(self.fragments):
            if job_size <= fragment:
                self.fragments[i] -= job_size
                return i, job_size  # Return the index of the allocated fragment and the allocated size
        return -1, 0  # Allocation failed

class Job:
    def __init__(self, job_id, start_time, required_size, execution_interval):
        self.job_id = job_id
        self.start_time = start_time
        self.required_size = required_size
        self.execution_interval = execution_interval
        self.allocated_block = None
        self.allocated_size = 0

class Node:
    def __init__(self):
        self.failed_allocation = False
        self.allocated_blocks = []  # List to store allocated blocks

    def diagnose_allocation(self):
        for i, fragment_size in enumerate(memory_manager.fragments):
            if fragment_size < 0:
                self.failed_allocation = True
                print(f"Allocation failed for Fragment {i + 1}.")
        if not self.failed_allocation:
            print("All allocations succeeded!")

    def report_allocated_blocks(self):
        if not self.failed_allocation:
            for i, size in self.allocated_blocks:
                print(f"Block {i + 1} allocated with size {size} KB.")
        else:
            print("Allocation failed for at least one fragment.")

def allocate_memory(jobs, file_fragments, file_size_kb):
    allocation = []  # Initialize a list to store the allocation results
    current_time = 0  # Initialize the current time
    file_in_memory = False  # Flag to track whether the file is in memory or not

    for job in jobs:
        if job.start_time > current_time:
            # Stop allocating when job.start_time is beyond the current_time
            if current_time >= 12 and not file_in_memory:
                # Transfer the file to memory at time interval 12
                file_allocated_block, file_allocated_size = memory_manager.allocate(file_size_kb)
                if file_allocated_block != -1:
                    allocation.append(("File", file_allocated_block, file_allocated_size))
                    file_in_memory = True
            current_time += 1  # Increment current_time
            continue

        if not file_in_memory:
            # If the file is not in memory, try to allocate its fragments
            for fragment in file_fragments:
                allocated_block, allocated_size = memory_manager.allocate(1)  # Allocate 1 Kbyte at a time
                if allocated_block != -1:
                    allocation.append(("File", allocated_block, allocated_size))
                else:
                    break  # Stop if allocation fails for any fragment

        allocated_block, allocated_size = memory_manager.allocate(job.required_size)
        if allocated_block != -1:
            allocation.append((f"Job {job.job_id}", allocated_block, allocated_size))
            job.allocated_block = allocated_block
            job.allocated_size = allocated_size
        else:
            allocation.append((f"Job {job.job_id}", -1, 0))
        
        current_time += job.execution_interval  # Increment current_time

    return allocation

def main():
    total_memory_size_kb = 20
    global memory_manager
    memory_manager = MemoryManager(total_memory_size_kb)

    # Define file information
    file_size_kb = 8
    file_fragments = [28, 5, 12, 13, 1, 4]

    # Create a list of jobs (as described in your example)
    jobs = [
        Job(1, 1, 2, 7),
        Job(2, 2, 3, 8),
        Job(3, 3, 4, 6),
        Job(4, 4, 3, 6),
        Job(5, 5, 2, 9),
        Job(6, 6, 3, 6),
        Job(7, 7, 2, 6),
    ]

    # Allocate memory for jobs and the file
    allocation_results = allocate_memory(jobs, file_fragments, file_size_kb)

    # Print allocation results and diagnose allocation
    for result in allocation_results:
        if result[1] != -1:
            print(f"{result[0]} allocated to Fragment {result[1]} with size {result[2]} KB")
        else:
            print(f"{result[0]} allocation failed.")

    node = Node()
    node.diagnose_allocation()
    node.report_allocated_blocks()

if __name__ == "__main__":
    main()
