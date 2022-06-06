from __future__ import annotations
from typing import Iterable, Iterator


class Process:
    "process"

    def __init__(self, pid: int, cycles: int, footprint: int) -> None:
        self.pid: int = pid
        self.cycles: int = cycles
        self.footprint: int = footprint
        self.cycles_left: int = cycles
        self.prev_process: Process = None
        self.next_process: Process = None
        self.arrival_time: float = None
        self.waiting_time: float = None
        self.turnaround_time: float = None

    def __str__(self) -> str:
        # for printing as string
        return f"Process #{self.pid} requiring {self.footprint}MB memory and {self.cycles}*10^6 cycles."

    @property
    def next(self) -> Process:
        "next prop"
        return self.next_process

    @next.setter
    def next(self, next_process: Process) -> None:
        "adding next process"
        # links both the forward and backward refernces in linked list
        next_process.prev_process = self
        self.next_process = next_process

    def calc(self):
        "calc"
        # calculates the waiting time and turnaround time based on previous processs 
        # in linked list when called
        self.waiting_time = (
            self.prev_process.turnaround_time - self.arrival_time
            if self.prev_process is not None
            else self.arrival_time
        )
        self.turnaround_time = self.waiting_time + self.cycles


class ProcessChain(Iterator, Iterable):
    "process chain"

    def __init__(self) -> None:
        self.head: Process = None
        self.tail: Process = None
        self.next: Process = None

    def __iter__(self):
        # iter and next are part of iterator and iterable protocols
        # use to make the chain iterable so that `for process in processor_chain` works
        self.next = self.head
        return self

    def __next__(self):
        if self.next is not None:
            x = self.next
            self.next = self.next.next
            return x
        raise StopIteration
    
    # adding and removing from linked list and node references
    def add(self, process: Process) -> None:
        "adding to chain"
        if self.head is None and self.tail is None:
            self.head = process
            self.tail = process
        else:
            self.tail.next = process
            self.tail = process

    def remove(self) -> Process:
        "removing from tail"
        if self.head is None and self.tail is None:
            return None
        if self.head is self.tail:
            process = self.head
            self.head = None
            self.tail = None
            return process
        process = self.tail
        process.prev_process.next_process = None
        self.tail = process.prev_process
        return process
