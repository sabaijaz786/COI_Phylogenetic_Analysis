from Bio import SeqIO

# Read the COI sequence
record = SeqIO.read("data/chimpanzee_COI.fasta", "fasta")

sequence = record.seq
length = len(sequence)

# Count each nucleotide
A = sequence.count("A")
T = sequence.count("T")
G = sequence.count("G")
C = sequence.count("C")

# Calculate percentages
A_percent = (A / length) * 100
T_percent = (T / length) * 100
G_percent = (G / length) * 100
C_percent = (C / length) * 100

GC_percent = ((G + C) / length) * 100

print("Species: Pan troglodytes")
print("Gene: COI")
print("Sequence length:", length)
print()

print("A:", A, f"({A_percent:.2f}%)")
print("T:", T, f"({T_percent:.2f}%)")
print("G:", G, f"({G_percent:.2f}%)")
print("C:", C, f"({C_percent:.2f}%)")
print()

print(f"GC content: {GC_percent:.2f}%")