from Bio import SeqIO

chimp = SeqIO.read(
    "data/chimpanzee_COI.fasta",
    "fasta"
)

mouse = SeqIO.read(
    "data/mouse_COI.fasta",
    "fasta"
)

print("Chimpanzee COI length:", len(chimp.seq))
print("Mouse COI length:", len(mouse.seq))

comparison_length = min(len(chimp.seq), len(mouse.seq))

differences = 0

for base1, base2 in zip(
    chimp.seq[:comparison_length],
    mouse.seq[:comparison_length]
):
    if base1 != base2:
        differences += 1

difference_percent = (differences / comparison_length) * 100

print("Comparison length:", comparison_length)
print("Number of nucleotide differences:", differences)
print(f"Percentage difference: {difference_percent:.2f}%")