from Bio import SeqIO

record = SeqIO.read(
    "data/orangutan_mitochondrial_genome.fasta",
    "fasta"
)

coi_sequence = record.seq[5341:6884]

coi_record = record[:]
coi_record.id = "Pongo_abelii_COI"
coi_record.name = "Pongo_abelii_COI"
coi_record.description = "Pongo abelii mitochondrial COI"

coi_record.seq = coi_sequence

SeqIO.write(
    coi_record,
    "data/orangutan_COI.fasta",
    "fasta"
)

print("Orangutan COI sequence extracted successfully!")
print("COI sequence length:", len(coi_record.seq))
print("COI sequence:")
print(coi_record.seq)