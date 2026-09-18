from Bio import SeqIO

# Read the complete mitochondrial genome
record = SeqIO.read("data/human_mitochondrial_genome.fasta", "fasta")

# COI coordinates from NCBI: 5904..7445
# Python uses 0-based indexing, so we use 5903 as the starting position.
coi_sequence = record.seq[5903:7445]

# Create a new sequence record
coi_record = record[:]
coi_record.id = "Homo_sapiens_COI"
coi_record.name = "Homo_sapiens_COI"
coi_record.description = "Homo sapiens mitochondrial COI"

coi_record.seq = coi_sequence

# Save the COI sequence as FASTA
SeqIO.write(coi_record, "data/human_COI.fasta", "fasta")

print("COI sequence extracted successfully!")
print("COI sequence length:", len(coi_record.seq))
print("COI sequence:")
print(coi_record.seq)