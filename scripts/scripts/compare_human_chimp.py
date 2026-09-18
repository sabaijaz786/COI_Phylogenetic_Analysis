from Bio import SeqIO

# Read the two COI sequences
human = SeqIO.read("data/human_COI.fasta", "fasta")
chimp = SeqIO.read("data/chimpanzee_COI.fasta", "fasta")

# Check that both sequences have the same length
if len(human.seq) != len(chimp.seq):
    print("Error: The sequences have different lengths.")
else:
    differences = 0

    for base1, base2 in zip(human.seq, chimp.seq):
        if base1 != base2:
            differences += 1

    length = len(human.seq)
    difference_percent = (differences / length) * 100

    print("Human COI length:", length)
    print("Chimpanzee COI length:", len(chimp.seq))
    print("Number of nucleotide differences:", differences)
    print(f"Percentage difference: {difference_percent:.2f}%")