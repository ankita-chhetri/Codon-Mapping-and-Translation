# About the Project

The **Codon Mapping and Translation** project is a simple Python program that translates DNA and RNA sequences into their corresponding amino acids.

In molecular biology, genetic information is stored in DNA and is used to produce proteins. During this process, nucleotides are read in groups of three, called codons. Each codon corresponds to a specific amino acid or acts as a stop signal during translation.

The main aim of this project is to understand how codons are mapped to amino acids using the standard genetic code and how this process can be implemented using Python.

I developed this project to improve my understanding of Python programming while applying it to a basic problem in bioinformatics.

# What Does the Program Do?

The program allows users to enter a DNA or RNA sequence and translates it into its corresponding amino acid sequence.

It uses a Python dictionary containing all 64 possible codons and their corresponding amino acids or stop signals. The program then reads the input sequence in groups of three nucleotides and uses this dictionary to perform the translation.

The program also checks whether the input sequence is valid, identifies start and stop codons, and handles incomplete codons at the end of a sequence.

For RNA sequences, the program converts uracil (U) to thymine (T) before using the same codon table for translation.

# Features

- **Codon Table:** Stores all 64 possible codons and their corresponding amino acids or stop signals in a Python dictionary.
- **Sequence Input:** Accepts DNA and RNA sequences directly from the user.
- **Input Validation:** Checks for invalid nucleotide characters and prevents DNA and RNA bases from being mixed in the same sequence.
- **Codon Formation:** Divides the sequence into groups of three nucleotides.
- **Amino Acid Translation:** Maps each codon to its corresponding amino acid using the standard genetic code.
- **Start and Stop Codon Detection:** Identifies the start codon (ATG) and stop codons (TAA, TAG, and TGA).
- **Translation Control:** Stops translation when the first stop codon is encountered.
- **Incomplete Codon Handling:** Detects and reports any leftover nucleotides that do not form a complete codon.
- **Codon Mapping Display:** Displays each translated codon alongside its corresponding amino acid.
- **Optional Codon Table Display:** Allows users to view the complete codon table if they want to.

# Technologies Used

- **Programming Language:** Python
- **Development Environment:** Visual Studio Code
- **Concepts Used:** Dictionaries, loops, conditional statements, string manipulation, input validation, and list operations.
- **Application Area:** Bioinformatics and basic biological sequence analysis.

No external Python libraries are required to run this program.

# How to Run the Program

Follow these steps to run the project on your computer:

1. Clone or download this repository from GitHub.
2. Open the project folder in Visual Studio Code.
3. Open the terminal in the project directory.
4. Run the following command:

   ```bash
   python Codon_table_generator.py
   ```

5. Enter a DNA or RNA sequence when the program asks for it.
6. Follow the on-screen instructions to view the translated sequence and other results.

# Example

**Input sequence:**

```text
ATGGCTTTTTAA
```

The program divides the sequence into four codons:

| Codon | Corresponding amino acid |
|---|---|
| ATG | Methionine |
| GCT | Alanine |
| TTT | Phenylalanine |
| TAA | Stop |

**Translated amino acid sequence:**

```text
Methionine - Alanine - Phenylalanine - Stop
```

The program also identifies ATG as the start codon and TAA as the stop codon.

# Handling Different Inputs

The program includes checks to handle different types of input.

For example, if a user enters an invalid character, the program displays an error message instead of attempting translation. If the sequence contains both T and U, the program rejects it because the input mixes DNA and RNA notation.

If the sequence ends with fewer than three nucleotides, the program reports the incomplete codon rather than translating it.

These checks help make the program more reliable and easier to use.

# Codon Table Comparison

The program implements the standard genetic code. Its codon assignments can be checked against established genetic-code references and Python implementations available online.

The following resources are useful for this comparison