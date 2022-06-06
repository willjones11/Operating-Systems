# import csv
# import random
# # import matplotlib.pyplot as plt

# def customNormalDistribution(upper_bound, lower_bound, mean, std_deviation):
#     value = int(random.gauss(mean, std_deviation))
#     result = value % (upper_bound - lower_bound + 1) + lower_bound
#     return result


# def average(list):
#     return sum(list) / len(list)

# # Parameter Declarations
# number_of_processes = 250

# # CPU Cycle Distribution Parameters
# cpu_upper_bound = 10e6
# cpu_lower_bound = 1
# cpu_mean = 10e3
# cpu_std_deviation = 10e3

# # Memory Requirement Distribution Parameters
# memory_upper_bound = 16 * 2**10
# memory_lower_bound = 1
# memory_mean = 8 * 2**10
# memory_std_deviation = 8 * 2**10

# process_list = []

# for i in range(number_of_processes):
#     cpu_cycles = customNormalDistribution(cpu_upper_bound, cpu_lower_bound, cpu_mean, cpu_std_deviation)
#     memory = customNormalDistribution(memory_upper_bound, memory_lower_bound, memory_mean, memory_std_deviation)

#     process = [i + 1, int(cpu_cycles), int(memory)]
#     process_list.append(process)

# # Open or Create File to Write Data
# with open('processes.csv', 'w', newline='') as csvfile:
#     # Initialize Writer Class
#     writer = csv.writer(csvfile)

#     # Write Column Headers
#     writer.writerow(['Process ID', 'CPU Cycles', 'Memory Requirement'])
#     # Write Process Data
#     writer.writerows(process_list)

# # # Select Values from CPU Cycles Column Only
# # cpu_cycles = [row[1] for row in process_list]

# # # Create Historgram of CPU Cycles
# # plt.hist(cpu_cycles, 10)
# # # Add Title and Axis Labels
# # plt.title("CPU Cycle Distribution")
# # plt.xlabel('CPU Cycles')
# # plt.ylabel('Frequency')
# # # Display Histogram
# # plt.show()

# # # Select Values from Memory Requirement Column Only
# # memory = [row[2] for row in process_list]

# # # Create Histogram of Memory Requirements
# # plt.hist(memory, 10)
# # # Add Title and Axis Labels
# # plt.title("Memory Distribution")
# # plt.xlabel('Memory Requirement')
# # plt.ylabel('Frequency')
# # # Display Histogram
# # plt.show()

# # # Print Calculated Average, Min Value & Max Value
# # print("CPU Cycles")
# # print("Average: ", average(cpu_cycles))
# # print("Min Value: ", min(cpu_cycles))
# # print("Max Value: ", max(cpu_cycles))

# # # Print Calculated Average, Min Value & Max Value
# # print("\nMemory Requirement")
# # print("Average: ", average(memory))
# # print("Min Value: ", min(memory))
# # print("Max Value: ", max(memory))
