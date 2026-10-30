# Codon Table Generator
# This program translates DNA or RNA sequences into amino acids.

def main():
    print("Welcome to the Codon Table Generator!")
    print("-------------------------------------")
    print("Translate a nucleotide sequence into amino acids.")

    # Step 1: Store the standard genetic code
    codon_table = {
        "TTT": "Phenylalanine", "TTC": "Phenylalanine",
        "TTA": "Leucine", "TTG": "Leucine",
        "TCT": "Serine", "TCC": "Serine",
        "TCA": "Serine", "TCG": "Serine",
        "TAT": "Tyrosine", "TAC": "Tyrosine",
        "TAA": "Stop", "TAG": "Stop",
        "TGT": "Cysteine", "TGC": "Cysteine",
        "TGA": "Stop", "TGG": "Tryptophan",

        "CTT": "Leucine", "CTC": "Leucine",
        "CTA": "Leucine", "CTG": "Leucine",
        "CCT": "Proline", "CCC": "Proline",
        "CCA": "Proline", "CCG": "Proline",
        "CAT": "Histidine", "CAC": "Histidine",
        "CAA": "Glutamine", "CAG": "Glutamine",
        "CGT": "Arginine", "CGC": "Arginine",
        "CGA": "Arginine", "CGG": "Arginine",

        "ATT": "Isoleucine", "ATC": "Isoleucine",
        "ATA": "Isoleucine", "ATG": "Methionine",
        "ACT": "Threonine", "ACC": "Threonine",
        "ACA": "Threonine", "ACG": "Threonine",
        "AAT": "Asparagine", "AAC": "Asparagine",
        "AAA": "Lysine", "AAG": "Lysine",
        "AGT": "Serine", "AGC": "Serine",
        "AGA": "Arginine", "AGG": "Arginine",

        "GTT": "Valine", "GTC": "Valine",
        "GTA": "Valine", "GTG": "Valine",
        "GCT": "Alanine", "GCC": "Alanine",
        "GCA": "Alanine", "GCG": "Alanine",
        "GAT": "Aspartic acid", "GAC": "Aspartic acid",
        "GAA": "Glutamic acid", "GAG": "Glutamic acid",
        "GGT": "Glycine", "GGC": "Glycine",
        "GGA": "Glycine", "GGG": "Glycine"
    }

    print("\nTotal codons in the dictionary:", len(codon_table))

    # Step 2: Ask the user for a DNA or RNA sequence
    sequence = input("\nEnter a DNA or RNA sequence: ")
    sequence = sequence.upper().strip()

    # Step 3: Validate the sequence
    if sequence == "":
        print("Please enter a sequence.")

    elif "T" in sequence and "U" in sequence:
        print("Invalid sequence: do not mix T and U.")

    elif not all(base in "ATGCU" for base in sequence):
        print("Invalid sequence. Use only A, T, G, C and U.")

    else:
        # Step 4: Convert RNA into DNA format if needed
        if "U" in sequence:
            print("\nRNA sequence detected.")
            sequence = sequence.replace("U", "T")
            print("RNA converted to DNA format for translation.")

        print("\nSequence entered:", sequence)

        # Step 5: Divide the sequence into codons
        codons = []

        for i in range(0, len(sequence), 3):
            codon = sequence[i:i + 3]

            if len(codon) == 3:
                codons.append(codon)
            else:
                incomplete_codon = codon

        if incomplete_codon:
            print("\nIncomplete codon at the end:", incomplete_codon)

        print("Number of complete codons:", len(codons))

        if incomplete_codon:
            print("Incomplete nucleotides:", len(incomplete_codon))
                

        for codon in codons:
            print(codon)

        # Step 6: Translate codons into amino acids
        amino_acids = []

        for codon in codons:
            amino_acid = codon_table[codon]
            amino_acids.append(amino_acid)

        print("\nTranslated Amino Acid Sequence:")
        print(" - ".join(amino_acids))

        # Step 7: Identify start and stop codons
        start_codon = "ATG"
        stop_codons = ["TAA", "TAG", "TGA"]

        if start_codon in codons:
            print("\nStart codon found: ATG")
        else:
            print("\nNo start codon found.")

        found_stop_codons = []

        for codon in codons:
            if codon in stop_codons:
                found_stop_codons.append(codon)

        if found_stop_codons:
            print(
                "Stop codon(s) found:",
                ", ".join(found_stop_codons)
            )
        else:
            print("No stop codon found.")

        # Step 8: Display the complete codon table
        print("\n" + "=" * 45)
        print("          STANDARD CODON TABLE")
        print("=" * 45)

        for codon, amino_acid in codon_table.items():
            print(f"{codon} : {amino_acid}")


# Start the program
main()