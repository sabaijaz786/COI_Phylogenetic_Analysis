from Bio import SeqIO

# Read the complete chimpanzee mitochondrial genome
record = SeqIO.read(
    "data/chimpanzee_mitochondrial_genome.fasta",
    "fasta"
)

# COX1 coordinates from NCBI: 5321..6862
# Python uses 0-based indexing
coi_sequence = record.seq[5320:6862]

# Create a new sequence record
coi_record = record[:]
coi_record.id = "Pan_troglodytes_COI"
coi_record.name = "Pan_troglodytes_COI"
coi_record.description = "Pan troglodytes mitochondrial COI"

coi_record.seq = coi_sequence

# Save the extracted COI sequence
SeqIO.write(
    coi_record,
    "data/chimpanzee_COI.fasta",
    "fasta"
)

print("Chimpanzee COI sequence extracted successfully!")
print("COI sequence length:", len(coi_record.seq))
print("COI sequence:")
print(coi_record.seq)