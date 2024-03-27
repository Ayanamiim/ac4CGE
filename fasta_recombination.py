def complement_sequence(sequence):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement.get(base, base) for base in sequence)

positive_file = r"datasets/pfur/pfur_pos_seq_test10.fasta"
negative_file = r"datasets/pfur/pfur_pos_seq_minus_test10.fasta"
output_file = r"datasets/pfur/pfur_Test_P.fasta"

def concatenate_fasta_files(positive_file, negative_file, output_file):
    with open(positive_file, "r") as pos_file, open(negative_file, "r") as neg_file, open(output_file, "w") as out_file:
        pos_sequences = pos_file.read().strip().split(">")[1:]
        neg_sequences = neg_file.read().strip().split(">")[1:]

        for pos_seq, neg_seq in zip(pos_sequences, neg_sequences):
            pos_header, pos_sequence = pos_seq.split("\n", 1)
            neg_header, neg_sequence = neg_seq.split("\n", 1)

            neg_complement = complement_sequence(neg_sequence.strip())

            combined_sequence = pos_sequence.strip() + neg_complement

            out_file.write(f">{pos_header}\n")
            out_file.write(f"{combined_sequence}\n")

concatenate_fasta_files(positive_file, negative_file, output_file)
