import matplotlib.pyplot as plt
from Bio import SeqIO

#get the 2 sequences from the seq_dotplot.fa and attribute them to var seq1 and seq2
record_iterator = SeqIO.parse("seq_dotplot.fa", "fasta")
seq1 = next(record_iterator)
seq2 = next(record_iterator)

def dotplot(seq1,seq2):
    matrix = [[0 for i in range(len(seq1))] for j in range(len(seq2))] #matrix
    if len(seq1)==len(seq2): #verifie si les deux sequences sont meme longueurs
        for x in range(len(seq1)): #for every nucleotide we verify if its the same
            for y in range(len(seq2)):
                if seq1[x]==seq2[y]:
                    matrix[x][y]=1

        img = plt.imshow(matrix, cmap="gray_r", origin='lower')

        #for the style
        cbar = plt.colorbar(img)
        cbar.set_label("Matching base (0 = no match, 1 = match)")
        font1 = {'family': 'serif', 'color': 'hotpink', 'size': 15}
        font2 = {'family': 'serif', 'size': 10}
        plt.title("Dotplot of two sequences",fontdict=font1)
        plt.xlabel("Sequence 1", fontdict=font2)
        plt.ylabel("Sequence 2", fontdict=font2)
        
        plt.show()

    return "it worked!"

dotplot(seq1,seq2)
