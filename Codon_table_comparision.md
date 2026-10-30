# Codon Table Comparison

# Objective
To compare the codon dictionary implemented in this project with an established genetic-code reference.

# References
1. NCBI — The Genetic Codes: https://www.ncbi.nlm.nih.gov/datasets/docs/v2/data-processing/taxonomy-processing/genetic-codes/
2. GitHub — Edinburgh Genome Foundry, Python Codon Tables: https://github.com/Edinburgh-Genome-Foundry/python_codon_tables

# Comparison Method
The project uses a Python dictionary containing 64 DNA codons and their corresponding amino acids or stop signals. The standard genetic code (NCBI Translation Table 1) is the reference.

Representative codons to check include ATG, TTT, GCT, TGG, TAA, TAG, and TGA.

# Expected Findings
The standard genetic code contains 64 codons: 61 encode amino acids and three are stop codons. ATG encodes methionine and is the standard start codon. TAA, TAG, and TGA are stop codons.

# Conclusion

The codon table used in this project follows the NCBI Standard Genetic Code (Table 1). The mappings were checked against the standard code, including codons that encode amino acids and the three stop codons: TAA, TAG, and TGA.

The standard genetic code contains 64 codons. Of these, 61 encode amino acids and 3 signal the termination of translation. ATG encodes methionine and is commonly used as a start codon.

This comparison helps verify the biological accuracy of the codon dictionary used by the program. The project uses the standard genetic code and does not currently support alternative genetic codes, such as mitochondrial codes.