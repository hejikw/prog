### DNA Analysis ###
import sys


### Read the nucleotides into a variable named "seq"

# Specify file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
filename = sys.argv[1]
inputfile = open(filename)

seq = ""
# Current line number = number of lines read so far
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    if linenum % 4 == 2:
        # Remove the newline from the end of the line
        line = line.rstrip()
        seq = seq + line


### Compute statistics

# Total nucleotides so far
total_count = 0
# Number of G and C nucleotides so far
gc_count = 0
at_count = 0

a_count = 0
t_count = 0
g_count = 0
c_count = 0

sum_count = 0

# for each base pair
for bp in seq:
    # increment total number of bps
    total_count = total_count + 1

    # next, if bp is a G or C,
    if bp == 'C' or bp == 'G':
        # increment the gc_count
        gc_count = gc_count + 1
    elif bp == 'A' or bp == 'T':
        at_count = at_count + 1
    
    if bp == 'A':
        a_count = a_count + 1
    elif bp == 'T':
        t_count = t_count + 1
    elif bp == 'G':
        g_count = g_count + 1
    elif bp == 'C':
        c_count = c_count + 1

sum_count = a_count + c_count + g_count + t_count
# divide gc_count by total_count
gc_content = float(gc_count) / sum_count
at_content = float(at_count) / sum_count

at_gc_ratio = (a_count + t_count) / (g_count + c_count)

# Print counts
print('GC-content:', gc_content)
print('AT-content:', at_content)
print('G count:', g_count)
print('C count:', c_count)
print('A count:', a_count)
print('T count:', t_count)
print('Sum count:', sum_count)
print('Total count:', total_count)
seq_length = len(seq)
print('seq length', seq_length)
print('AT/GC Ratio:', at_gc_ratio)

def classify(gc_content):
    if gc_content > .60:
        classification = "high GC content"
    elif gc_content >= .40 and gc_content <= .60:
        classification = "moderate GC content"
    else:
        classification = "low GC content"
    return classification

print("GC Classification:", classify(gc_content))
