import csv
from process_class import Process

# reads data from CSV and loads into an array of Processes

def data():
    "data"
    processes = []

    with open("processes.csv", encoding="utf8") as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile)
        for pid, cycles, footprint in reader:
            processes.append(
                Process(pid=int(pid), cycles=int(cycles), footprint=int(footprint))
            )
    return processes
