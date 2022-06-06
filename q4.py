from typing import List
from process_class import Process, ProcessChain
from data_loader import data


def fifo_big_little_memory():
    "fifo modded"
    processes: List[Process] = data() # no sort, only change from q3
    for process in processes:
        process.arrival_time = 0
    slow_processor_chains: List[ProcessChain] = [ProcessChain() for _ in range(3)]
    fast_processor_chains: List[ProcessChain] = [ProcessChain() for _ in range(3)]
    for i, c_process in enumerate(processes[:3]):  # from the start
        slow_processor_chains[i].add(process=c_process)
        c_process.calc()
    for i, c_process in enumerate(processes[3:6]):  # from the end
        fast_processor_chains[i].add(process=c_process)
        faster_calc(c_process)

    rem_processes = processes[6:]
    current_time = 0
    skip_append = False # when true, only 4ghz 16GB processors can run remaining processes
    while rem_processes:
        slow_fastest_done = min(slow_processor_chains, key=lambda x: x.tail.cycles_left)
        fast_fastest_done = min(fast_processor_chains, key=lambda x: x.tail.cycles_left)
        slow_true = (
            slow_fastest_done.tail.cycles_left < fast_fastest_done.tail.cycles_left
        ) if not skip_append else False
        next_process = rem_processes.pop(0)
        curr_len = len(rem_processes)
        if slow_true:
            checking = True
            while checking: # changes process to one with a lower footprint if > max ram of lower
                if next_process.footprint > 8 * 2**10:
                    rem_processes.append(next_process)
                    next_process = rem_processes.pop(0)
                    curr_len -= 1
                    if curr_len < 0:
                        skip_append = True
                        checking = False
                        rem_processes.append(next_process)
                else:
                    checking = False
        # logic to get from the heavier processes if 4ghz processor is done
        index_done = (
            slow_processor_chains.index(slow_fastest_done)
            if slow_true
            else fast_processor_chains.index(fast_fastest_done)
        )
        current_time = (
            slow_fastest_done.tail.turnaround_time
            if slow_true
            else fast_fastest_done.tail.turnaround_time
        )
        for processor_chain in slow_processor_chains:
            process = processor_chain.tail
            process.cycles_left = process.cycles + process.waiting_time - current_time
            if skip_append and process.cycles_left < 0:
                process.cycles_left = 0
        for processor_chain in fast_processor_chains:
            process = processor_chain.tail
            process.cycles_left = (
                process.cycles + process.waiting_time - current_time
            ) // 2
        if slow_true:
            if not skip_append:
                slow_processor_chains[index_done].add(next_process)
                next_process.calc()
        else:
            fast_processor_chains[index_done].add(next_process)
            faster_calc(next_process)
    print(current_time)
    return slow_processor_chains + fast_processor_chains


def faster_calc(process: Process) -> None:
    "calc for 4ghz processor"
    process.calc()
    process.cycles_left //= 2
    process.turnaround_time -= process.cycles // 2


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


print("Fifo_big_little_memory_restricted")
evaluation(fifo_big_little_memory())
