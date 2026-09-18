from Bio import SeqIO

record = SeqIO.read(
    "data/mouse_mitochondrial_genome.fasta",
    "fasta"
)

coi_sequence = record.seq[5327:6872]

coi_record = record[:]
coi_record.id = "Mus_musculus_COI"
coi_record.name = "Mus_musculus_COI"
coi_record.description = "Mus musculus mitochondrial COI"

coi_record.seq = coi_sequence

SeqIO.write(
    coi_record,
    "data/mouse_COI.fasta",
    "fasta"
)

print("Mouse COI sequence extracted successfully!")
print("COI sequence length:", len(coi_record.seq))
print("COI sequence:")
print(coi_record.seq)