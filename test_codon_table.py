from Codon_table_generator import codon_table

# Test 1: Check that all 64 codons are present
def test_codon_count():
    assert len(codon_table) == 64


# Test 2: Check the start codon
def test_start_codon():
    assert codon_table["ATG"] == "Methionine"


# Test 3: Check all three stop codons
def test_stop_codons():
    assert codon_table["TAA"] == "Stop"
    assert codon_table["TAG"] == "Stop"
    assert codon_table["TGA"] == "Stop"


# Test 4: Check selected amino-acid mappings
def test_amino_acid_mapping():
    assert codon_table["GCT"] == "Alanine"
    assert codon_table["TTT"] == "Phenylalanine"
    assert codon_table["TGG"] == "Tryptophan"


# Run all tests
test_codon_count()
test_start_codon()
test_stop_codons()
test_amino_acid_mapping()

print("All codon table tests passed!")