from Bio import SeqIO

chimp = SeqIO.read("data/chimpanzee_COI.fasta", "fasta")
gorilla = SeqIO.read("data/gorilla_COI.fasta", "fasta")

print("Chimpanzee COI length:", len(chimp.seq))
print("Gorilla COI length:", len(gorilla.seq))

# Compare positions shared by both sequences
comparison_length = min(len(chimp.seq), len(gorilla.seq))

differences = 0

for base1, base2 in zip(
    chimp.seq[:comparison_length],
    gorilla.seq[:comparison_length]
):
    if base1 != base2:
        differences += 1

difference_percent = (differences / comparison_length) * 100

print("Comparison length:", comparison_length)
print("Number of nucleotide differences:", differences)
print(f"Percentage difference: {difference_percent:.2f}%")