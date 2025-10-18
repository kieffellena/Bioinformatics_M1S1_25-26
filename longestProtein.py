#dna_sequence = str(input("Enter DNA sequence: "))

_GENETIC_CODE = {
                    # Phenylalanine / Leucine
                    "TTT":"F","TTC":"F","TTA":"L","TTG":"L",
                    # Serine
                    "TCT":"S","TCC":"S","TCA":"S","TCG":"S",
                    # Tyrosine / Stop
                    "TAT":"Y","TAC":"Y","TAA":"*","TAG":"*",
                    # Cysteine / Stop / Tryptophan
                    "TGT":"C","TGC":"C","TGA":"*","TGG":"W",
                    # Leucine
                    "CTT":"L","CTC":"L","CTA":"L","CTG":"L",
                    # Proline
                    "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
                    # Histidine / Glutamine
                    "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
                    # Arginine
                    "CGT":"R","CGC":"R","CGA":"R","CGG":"R",
                    # Isoleucine / Methionine (start)
                    "ATT":"I","ATC":"I","ATA":"I","ATG":"M",
                    # Threonine
                    "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
                    # Asparagine / Lysine
                    "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
                    # Serine / Arginine
                    "AGT":"S","AGC":"S","AGA":"R","AGG":"R",
                    # Valine
                    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
                    # Alanine
                    "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
                    # Aspartate / Glutamate
                    "GAT":"D","GAC":"D","GAA":"E","GAG":"E",
                    # Glycine
                    "GGT":"G","GGC":"G","GGA":"G","GGG":"G",
                }

#dna complementaire
def complement(dna_sequence) :
                    dna_sequence = dna_sequence.upper()
                    dna_sequence_reverse=""
                    for i in dna_sequence :
                        if i == 'A':
                            dna_sequence_reverse+='T'
                        elif i == 'T':
                            dna_sequence_reverse+='A'
                        elif i == 'G':
                            dna_sequence_reverse+='C'
                        elif i== 'C':
                            dna_sequence_reverse+='G'
                        else :
                            print("Pas la bonne sequence")
                            break
                    return dna_sequence_reverse[::-1]

#6 readingsframes diff
def readingframe(dna_sequence):
                    r = []
                    r1 = [dna_sequence[i:i + 3] for i in range(0, len(dna_sequence), 3)]
                    r2 = [dna_sequence[i:i + 3] for i in range(1, len(dna_sequence), 3)]
                    r3 = [dna_sequence[i:i + 3] for i in range(2, len(dna_sequence), 3)]

                    dna_sequence_comp = complement(dna_sequence)
                    r4 = [dna_sequence_comp[i:i + 3] for i in range(0, len(dna_sequence), 3)]
                    r5 = [dna_sequence_comp[i:i + 3] for i in range(1, len(dna_sequence), 3)]
                    r6 = [dna_sequence_comp[i:i + 3] for i in range(2, len(dna_sequence), 3)]

                    r.extend([r1, r2, r3, r4, r5, r6])
                    return r

#si le codon a 3 nucleoides il cherche lacide amine correspondant dans le dico
def translate_frame(frame):
                    acid = ""
                    for codon in frame:
                        if len(codon) == 3:
                            acid += _GENETIC_CODE.get(codon, "X") #X si pas dans le dico
                    return acid

def get_proteins_from_frame(protein_seq):
                    proteins = []
                    current_prot = "" #la proteine en train detre regarde

                    for aa in protein_seq:
                        if aa == "*": #si cest stop
                            if current_prot:  # si il y a une nouvelle proteine
                                proteins.append(current_prot)
                                current_prot = ""  # on recommence apres stop
                        else:
                            current_prot += aa  # on ajoute l'acid a la prot

                    #cas si prot se termine
                    if current_prot:
                        proteins.append(current_prot)

                    return proteins


def translate_frames(dna_sequence):
                    r1, r2, r3, r4, r5, r6 = readingframe(dna_sequence)

                    #traduis chaque frame en acide
                    t_r1 = translate_frame(r1)
                    t_r2 = translate_frame(r2)
                    t_r3 = translate_frame(r3)
                    t_r4 = translate_frame(r4)
                    t_r5 = translate_frame(r5)
                    t_r6 = translate_frame(r6)

                    #recup des prot des frames en acide
                    all_proteins = []
                    for t_frame in [t_r1, t_r2, t_r3, t_r4, t_r5, t_r6]:
                        all_proteins.extend(get_proteins_from_frame(t_frame))

                    #prot la plus longue
                    longest_protein = max(all_proteins, key=len) #chercghe a travers tt
                    print("Longest protein sequence:", longest_protein)
                    return longest_protein

                ############################
dna_sequence = "CAGCAGCTTGGCAACATTCTGTAAAAGCAGCTTTATACCTTTTAGCAAAGAAAAGGAGTTCCGGGGCATAAAAGTAAGGATGTCTTCTGGCAATTTCATATAAGTATTTTTTCAAAAATGTCTCTTCATTGTCATGAAAAGCAGTGCACATCACATCAACCTCTGGTCTCACCAATCGGGGGAGGTTTGGGTTGTCATCTTTGTGTTGCAAGAAGCATTCATTTCTCTCAGGTTCTTGTTTTGCACAGCAGTCAGCCATTTCACCATAGGTTTCACGAAGAGTTGCAACTGTGCATAATTTGTCTCCAAAAAGGGTATGAAGTGATTTGTCACAATTTTCAGCTGACTCATCAGCAACACATGTTTTTGCAAATTCAGTTACTTCATTCACTAATTTTACATGATCTTCAAATGGACACTGCTGAAGATACTGAGCAAAGGCAATCAACACCAAGGCTTTGAAATTTTCTTCTCCCAAATCTTTAAACCGATGAGCAACCTCACTCTTGTGTGCATCTCGACGAAACACACCCCTGGAATAAGCCGAGCTAAAG"

translate_frames(dna_sequence)