import random
import numpy as np
from Bio import Align
from Bio.Align import substitution_matrices
import matplotlib.pyplot as plt

#generate n permutations of V
def shuffle(v,n) :
    shuff = []
    ind = np.arange(len(v))
    for i in range(n):
        random.shuffle(ind)
        tmp = "".join([v[j] for j in ind])
        shuff.append(tmp)
    return(shuff)

#algin each permuted seq to U and add score
def align(shuff, u):
    align = []
    aligner = Align.PairwiseAligner()
    aligner.mode = 'local'
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")

    aligner.query_open_gap_score = -10
    aligner.query_extend_gap_score = -0.5
    aligner.target_open_gap_score = -10
    aligner.target_extend_gap_score = -0.5

    for seq in shuff:
        aln = aligner.align(seq, u)[0]   # premier alignement
        align.append({
            "permutation": seq,
            "alignment": str(aln),
            "score": aln.score
        })
    return align

#plot the distribution of the alignements scores
def dotplot(align):
    #pour chaque seq extraire le score.
    scores = [a["score"] for a in align]
    seqs = [a["permutation"] for a in align]

    plt.figure(figsize=(8,5))
    plt.scatter(range(len(scores)), scores, color="hotpink", marker="o")

    # style
    font1 = {'family': 'serif', 'color': 'hotpink', 'size': 15}
    font2 = {'family': 'serif', 'size': 10}
    plt.title("distribution of the alignment scores obtained from the permuted sequences", fontdict=font1)
    plt.xlabel("Permutation", fontdict=font2)
    plt.ylabel("Scores", fontdict=font2)

    plt.xticks(range(len(seqs)), seqs, rotation=45)
    plt.tight_layout()

    plt.show()
    return "it worked!"

v = "ABC"
u = "CDBA"

shuff = shuffle(v,3)
#print(f"shuff : ",shuff[:3])

align = align(shuff,u)
#print(f"alignement :",align)

dotplot(align)