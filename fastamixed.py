from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import random

def shuffle_fasta_sequences(file1, file2, output_file):
    records1 = list(SeqIO.parse(file1, "fasta"))
    records2 = list(SeqIO.parse(file2, "fasta"))

    random.shuffle(records1)
    random.shuffle(records2)

    output_handle = open(output_file, "w")

    for i, record in enumerate(records1):
        record.id = record.id.split("|")[0] + "|1"
        SeqIO.write(record, output_handle, "fasta")
    for i, record in enumerate(records2):
        record.id = record.id.split("|")[0] + "|0"
        SeqIO.write(record, output_handle, "fasta")

    output_handle.close()

fasta_file1 = r"datasets/pfur/pfur_Test_P10.fasta"
fasta_file2 = r"datasets/pfur/pfur_Test_N10.fasta"
output_file = r"datasets/pfur/pfur_Test10.fasta"

shuffle_fasta_sequences(fasta_file1, fasta_file2, output_file)
