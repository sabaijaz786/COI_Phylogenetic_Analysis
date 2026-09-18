from Bio import SeqIO

orangutan = SeqIO.read(
    "data/orangutan_COI.fasta",
    "fasta"
)

mouse = SeqIO.read(
    "data/mouse_COI.fasta",
    "fasta"
)

print("Orangutan COI length:", len(orangutan.seq))
print("Mouse COI length:", len(mouse.seq))

comparison_length = min(len(orangutan.seq), len(mouse.seq))

differences = 0

for base1, base2 in zip(
    orangutan.seq[:comparison_length],
    mouse.seq[:comparison_length]
):
    if base1 != base2:
        differences += 1

difference_percent = (differences / comparison_length) * 100

print("Comparison length:", comparison_length)
print("Number of nucleotide differences:", differences)
print(f"Percentage difference: {difference_percent:.2f}%")