# Bioinformatics_M1S1_25-26
This repository contains small Python programs developed during my bioinformatics coursework from my Master's *Data Management in Biosciences*

---

## Contents

1. **Sequence Comparison and Dot Plot**
2. **DNA Translation and Protein Extraction**

---

## 1. Sequence Comparison and Dot Plot

**Aim:**  
Generate a similarity matrix between two sequences and visualize regions of similarity using a dot plot.

**Description:**  
This project reads sequences from a FASTA (.fa) file, computes a comparison matrix between them, and generates a dot plot to visualize regions of similarity.

---

## 2. DNA Translation and Protein Extraction

**Description:**  
This script reads a DNA sequence, generates its complementary strand, computes all six possible reading frames and translates each frame into its corresponding amino acid sequence using the standard genetic code.
It then identifies all possible protein sequences and outputs the longest protein found across all reading frames.
This script intentionally does not restrict translation to sequences starting with a start codon. This approach is useful, allowing analysis of potentially incomplete or unannotated regions.
