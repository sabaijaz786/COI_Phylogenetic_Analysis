from Bio import SeqIO

gorilla = SeqIO.read(
    "data/gorilla_COI.fasta",
    "fasta"
)

rhesus = SeqIO.read(
    "data/rhesus_macaque_COI.fasta",
    "fasta"
)

print("Gorilla COI length:", len(gorilla.seq))
print("Rhesus macaque COI length:", len(rhesus.seq))

comparison_length = min(len(gorilla.seq), len(rhesus.seq))

differences = 0

for base1, base2 in zip(
    gorilla.seq[:comparison_length],
    rhesus.seq[:comparison_length]
):
    if base1 != base2:
        differences += 1

difference_percent = (differences / comparison_length) * 100

print("Comparison length:", comparison_length)
print("Number of nucleotide differences:", differences)
print(f"Percentage difference: {difference_percent:.2f}%")