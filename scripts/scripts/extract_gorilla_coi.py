from Bio import SeqIO

record = SeqIO.read(
    "data/gorilla_mitochondrial_genome.fasta",
    "fasta"
)

coi_sequence = record.seq[5324:6875]

coi_record = record[:]
coi_record.id = "Gorilla_gorilla_COI"
coi_record.name = "Gorilla_gorilla_COI"
coi_record.description = "Gorilla gorilla mitochondrial COI"

coi_record.seq = coi_sequence

SeqIO.write(
    coi_record,
    "data/gorilla_COI.fasta",
    "fasta"
)

print("Gorilla COI sequence extracted successfully!")
print("COI sequence length:", len(coi_record.seq))
print("COI sequence:")
print(coi_record.seq)