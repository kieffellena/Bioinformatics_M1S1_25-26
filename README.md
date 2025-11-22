# Bioinformatics_M1S1_25-26
This repository contains small Python programs developed during my bioinformatics coursework for my Master's *Data Management in Biosciences*, Professor Marie-Joe Karam Kassar.


## Contents

1. **Sequence Comparison and Dot Plot**
2. **DNA Translation and Protein Extraction**
3. **Tutorial Pairwise Sequence Alignment**

## 1. Sequence Comparison and Dot Plot

**Aim:**  
Generate a similarity matrix between two sequences and visualize regions of similarity using a dot plot.

**Description:**  
This project reads sequences from a FASTA (.fa) file, computes a comparison matrix between them, and generates a dot plot to visualize regions of similarity.

## 2. DNA Translation and Protein Extraction
**Aim:** 
Identifying the longest protein found across all reading frames. 

**Description:**  
This script reads a DNA sequence, generates its complementary strand, computes all six possible reading frames and translates each frame into its corresponding amino acid sequence using the standard genetic code.
It then identifies all possible protein sequences and outputs the longest protein found across all reading frames.
This script intentionally does not restrict translation to sequences starting with a start codon. This approach is useful, allowing analysis of potentially incomplete or unannotated regions.

## 3. Tutorial Pairwise Sequence Alignment
**Aim:** 
Assess the significance of alignment. 

**Description:** 
This script generates n permutations of V (protein sequence), each having the same length and residue composition as the original
sequence, then align each permuted sequence to U (other protein sequence) using the same alignment method. It then computes the alignment score for each of these alignments & plots the distribution of the alignment scores obtained from the permuted sequences. Afterwards, it counts the number of permutations whose alignment scores satisfy s_permutation_i ≥ s. This gives an empirical estimate of how likely the observed score s is to occur by chance.



