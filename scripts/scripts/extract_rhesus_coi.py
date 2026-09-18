from Bio import SeqIO

record = SeqIO.read(
    "data/rhesus_macaque_mitochondrial_genome.fasta",
    "fasta"
)

coi_sequence = record.seq[5316:6885]

coi_record = record[:]
coi_record.id = "Macaca_mulatta_COI"
coi_record.name = "Macaca_mulatta_COI"
coi_record.description = "Macaca mulatta mitochondrial COI"

coi_record.seq = coi_sequence

SeqIO.write(
    coi_record,
    "data/rhesus_macaque_COI.fasta",
    "fasta"
)

print("Rhesus macaque COI sequence extracted successfully!")
print("COI sequence length:", len(coi_record.seq))
print("COI sequence:")
print(coi_record.seq)