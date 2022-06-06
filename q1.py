from typing import List
from process_class import Process, ProcessChain
from data_loader import data


def fifo():
    "fifo"
    processes: List[Process] = data()
    for process in processes:
        process.arrival_time = 0 # all processeshave already arrived
    processor_chains: List[ProcessChain] = [ProcessChain() for _ in range(6)]
    for i, c_process in enumerate(processes[:6]):
        processor_chains[i].add(process=c_process)
        c_process.calc()

    rem_processes = processes[6:]
    current_time = 0
    while rem_processes:
        next_process = rem_processes.pop(0)
        # this checks which process is done and then increments that time, decrements those cycles,
        # and adds the new process to the free processor's chain
        fastest_done = min(processor_chains, key=lambda x: x.tail.cycles_left)
        current_time = fastest_done.tail.turnaround_time
        for processor_chain in processor_chains:
            process = processor_chain.tail
            process.cycles_left = process.cycles + process.waiting_time - current_time
        fastest_done_index = processor_chains.index(fastest_done)
        processor_chains[fastest_done_index].add(next_process)
        next_process.calc()
    print(current_time)
    return processor_chains


def sjf():
    "sjf"
    processes: List[Process] = data()
    processes.sort(key=lambda x: x.cycles)  # only change between fifo and sjf
    for process in processes:
        process.arrival_time = 0
    processor_chains: List[ProcessChain] = [ProcessChain() for _ in range(6)]
    for i, c_process in enumerate(processes[:6]):
        processor_chains[i].add(process=c_process)
        c_process.calc()
    rem_processes = processes[6:]
    current_time = 0
    while rem_processes:
        next_process = rem_processes.pop(0)
        fastest_done = min(processor_chains, key=lambda x: x.tail.cycles_left)
        current_time = fastest_done.tail.turnaround_time
        for processor_chain in processor_chains:
            process = processor_chain.tail
            process.cycles_left = process.cycles + process.waiting_time - current_time
        fastest_done_index = processor_chains.index(fastest_done)
        processor_chains[fastest_done_index].add(next_process)
        next_process.calc()
    print(current_time)
    return processor_chains


def r_r():
    "round robin"
    processes: List[Process] = data()
    for process in processes:
        process.arrival_time = 0
    processor_chains: List[ProcessChain] = [ProcessChain() for _ in range(6)]
    for i, c_process in enumerate(processes[:6]):
        processor_chains[i].add(process=c_process)
    rem_processes = processes[6:]
    quantum = 1000 # time quantum
    current_time = [0 for _ in range(6)] # array of times because processors may be out of sync
                                         # when the cycles left of current porcess is less than quantum
    while rem_processes:
        for i, processor_chain in enumerate(processor_chains):
            process = processor_chain.tail
            # if there are no cycles left after quantum,
            # the turnaround and waiting time is calculated and that porcess is removed from list
            # else it is removed and placed in the back
            # of the array and a new process is given to the processor
            if process.cycles_left <= quantum:
                current_time[i] += process.cycles_left
                process.waiting_time = (
                    current_time[i] - process.cycles + process.cycles_left
                )
                process.cycles_left = 0
                process.turnaround_time = process.waiting_time + process.cycles
                if rem_processes:
                    new_process = rem_processes.pop(0)
                    processor_chains[i].add(new_process)
            else:
                current_time[i] += quantum
                process.cycles_left -= quantum
                if rem_processes:
                    processor_chains[i].remove()
                    rem_processes.append(process)
                    new_process = rem_processes.pop(0)
                    processor_chains[i].add(new_process)
    for i, processor_chain in enumerate(processor_chains):
        process = processor_chain.tail
        process.waiting_time = current_time[i] - process.cycles + process.cycles_left
        process.cycles_left = 0
        process.turnaround_time = process.waiting_time + process.cycles
        # process.cycles_left = process.cycles + process.waiting_time - current_time
        # fastest_done_index = processor_chains.index(fastest_done)
        # processor_chains[fastest_done_index].add(next_process)
    print(current_time)
    return processor_chains


def evaluation(processor_chains: List[ProcessChain]):
    "eval"
    index = 1
    for processor_chain in processor_chains:
        num_processes = 0
        total_wait = 0
        total_turnaround = 0
        for process in processor_chain:
            num_processes += 1
            total_wait += process.waiting_time
            total_turnaround += process.turnaround_time

        print(
            f"Processor {index} had {num_processes} processes, avg wait time {total_wait/num_processes:.2f} cycles, avg turnaround time {total_turnaround/num_processes:.2f} cycles"
        )
        index += 1


print("fifo")
evaluation(fifo())
print("sjf")
evaluation(sjf())
print("rr")
evaluation(r_r())
