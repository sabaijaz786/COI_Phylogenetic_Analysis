from Bio import SeqIO

chimp = SeqIO.read(
    "data/chimpanzee_COI.fasta",
    "fasta"
)

rhesus = SeqIO.read(
    "data/rhesus_macaque_COI.fasta",
    "fasta"
)

print("Chimpanzee COI length:", len(chimp.seq))
print("Rhesus macaque COI length:", len(rhesus.seq))

comparison_length = min(len(chimp.seq), len(rhesus.seq))

differences = 0

for base1, base2 in zip(
    chimp.seq[:comparison_length],
    rhesus.seq[:comparison_length]
):
    if base1 != base2:
        differences += 1

difference_percent = (differences / comparison_length) * 100

print("Comparison length:", comparison_length)
print("Number of nucleotide differences:", differences)
print(f"Percentage difference: {difference_percent:.2f}%")