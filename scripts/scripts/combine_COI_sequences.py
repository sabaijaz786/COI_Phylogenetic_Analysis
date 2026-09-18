from Bio import SeqIO

files = [
    "data/human_COI.fasta",
    "data/chimpanzee_COI.fasta",
    "data/gorilla_COI.fasta",
    "data/orangutan_COI.fasta",
    "data/rhesus_macaque_COI.fasta",
    "data/mouse_COI.fasta"
]

records = []

for file in files:
    record = SeqIO.read(file, "fasta")
    records.append(record)

SeqIO.write(
    records,
    "data/all_six_COI_sequences.fasta",
    "fasta"
)

print("All six COI sequences combined successfully!")
print("Number of sequences:", len(records))

for record in records:
    print(record.id, "-", len(record.seq), "bp")