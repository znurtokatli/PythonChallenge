import os
import csv

#  define variables
total_votes = 0
candidates = {}

# change directory to the current file path and get source file path
os.chdir(os.path.dirname(__file__))
source_file_path = os.path.join("Resources", "election_data.csv" )

# open source file
with open(source_file_path, newline="") as csvfile:

    # file reader
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # read rows
    for row in csv_reader:

        total_votes += 1
        candidate_name = row[2]

        # candidate is exists in dictionary then increase vote value
        if candidate_name in candidates.keys():
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# export a text file with the results
output_file = os.path.join("Analysis", "Analysis.txt")
with open(output_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("----------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("----------------\n")

    for name, count in candidates.items():
        outfile.write(f"{name}: {((count/total_votes) * 100):.3f}% ({count})\n")

    outfile.write("----------------\n")
    outfile.write(f"Winner: {max(candidates, key=candidates.get)}\n")
    outfile.write("----------------\n")


# print the analysis to the terminal
print("Election Results")
print("----------------")
print(f"Total Votes: {total_votes}")
print("----------------")

for name, count in candidates.items():
    print(f'{name}: {((count/total_votes) * 100):.3f}% ({count})')

print("----------------")
print(f"{max(candidates, key=candidates.get)}")
print("----------------")
