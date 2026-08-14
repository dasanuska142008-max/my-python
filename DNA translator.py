codons= {
    # U - First Base
    "UUU": "Phenylalanine (Phe)", "UUC": "Phenylalanine (Phe)",
    "UUA": "Leucine (Leu)", "UUG": "Leucine (Leu)",
    "UCU": "Serine (Ser)", "UCC": "Serine (Ser)",
    "UCA": "Serine (Ser)", "UCG": "Serine (Ser)",
    "UAU": "Tyrosine (Tyr)", "UAC": "Tyrosine (Tyr)",
    "UAA": "STOP", "UAG": "STOP",
    "UGU": "Cysteine (Cys)", "UGC": "Cysteine (Cys)",
    "UGA": "STOP", "UGG": "Tryptophan (Trp)",

    # C - First Base
    "CUU": "Leucine (Leu)", "CUC": "Leucine (Leu)",
    "CUA": "Leucine (Leu)", "CUG": "Leucine (Leu)",
    "CCU": "Proline (Pro)", "CCC": "Proline (Pro)",
    "CCA": "Proline (Pro)", "CCG": "Proline (Pro)",
    "CAU": "Histidine (His)", "CAC": "Histidine (His)",
    "CAA": "Glutamine (Gln)", "CAG": "Glutamine (Gln)",
    "CGU": "Arginine (Arg)", "CGC": "Arginine (Arg)",
    "CGA": "Arginine (Arg)", "CGG": "Arginine (Arg)",

    # A - First Base
    "AUU": "Isoleucine (Ile)", "AUC": "Isoleucine (Ile)",
    "AUA": "Isoleucine (Ile)", "AUG": "Methionine (Met) / START",
    "ACU": "Threonine (Thr)", "ACC": "Threonine (Thr)",
    "ACA": "Threonine (Thr)", "ACG": "Threonine (Thr)",
    "AAU": "Asparagine (Asn)", "AAC": "Asparagine (Asn)",
    "AAA": "Lysine (Lys)", "AAG": "Lysine (Lys)",
    "AGU": "Serine (Ser)", "AGC": "Serine (Ser)",
    "AGA": "Arginine (Arg)", "AGG": "Arginine (Arg)",

    # G - First Base
    "GUU": "Valine (Val)", "GUC": "Valine (Val)",
    "GUA": "Valine (Val)", "GUG": "Valine (Val)",
    "GCU": "Alanine (Ala)", "GCC": "Alanine (Ala)",
    "GCA": "Alanine (Ala)", "GCG": "Alanine (Ala)",
    "GAU": "Aspartic Acid (Asp)", "GAC": "Aspartic Acid (Asp)",
    "GAA": "Glutamic Acid (Glu)", "GAG": "Glutamic Acid (Glu)",
    "GGU": "Glycine (Gly)", "GGC": "Glycine (Gly)",
    "GGA": "Glycine (Gly)", "GGG": "Glycine (Gly)"
}
dna = input("Enter DNA coding strand: ").upper()

mrna = dna.replace("T", "U")




for i in range(0, len(mrna), 3):
    x = mrna[i]
    y = mrna[i+1]
    z = mrna[i+2] 
    
    if x+y+z== "AUG":
        print("START CODON")
    elif x+y+z == "UAA" or x+y+z == "UAG" or x+y+z == "UGA":
        print("STOP CODON")
    elif x+y+z == "UUU" or x+y+z == "UUC":
        print("Phenylalanine (Phe)")
    elif x+y+z == "UUA" or x+y+z == "UUG":
        print("Leucine (Leu)")
    elif x+y+z == "UCU" or x+y+z == "UCC" or x+y+z == "UCA" or x+y+z == "UCG":
        print("Serine (Ser)")
    elif x+y+z == "UAU" or x+y+z == "UAC":
        print("Tyrosine (Tyr)")
    elif x+y+z == "UGU" or x+y+z == "UGC":
        print("Cysteine (Cys)")
    elif x+y+z == "CUU" or x+y+z == "CUC" or x+y+z == "CUA" or x+y+z == "CUG":
        print("Leucine (Leu)")
    elif x+y+z == "CCU" or x+y+z == "CCC" or x+y+z == "CCA" or x+y+z == "CCG":
        print("Proline (Pro)")
    elif x+y+z == "CAU" or x+y+z == "CAC":
        print("Histidine (His)")
    elif x+y+z == "CAA" or x+y+z == "CAG":
        print("Glutamine (Gln)")
    elif x+y+z == "CGU" or x+y+z == "CGC" or x+y+z == "CGA" or x+y+z == "CGG":
        print("Arginine (Arg)")
    elif x+y+z == "AUU" or x+y+z == "AUC" or x+y+z == "AUA":
        print("Isoleucine (Ile)")
    elif x+y+z == "AUG":
        print("Methionine (Met) / START")
    elif x+y+z == "ACU" or x+y+z == "ACC" or x+y+z == "ACA" or x+y+z == "ACG":
        print("Threonine (Thr)")
    elif x+y+z == "AAU" or x+y+z == "AAC":
        print("Asparagine (Asn)")
    elif x+y+z == "AAA" or x+y+z == "AAG":
        print("Lysine (Lys)")
    elif x+y+z == "AGU" or x+y+z == "AGC":
        print("Serine (Ser)")
    elif x+y+z == "AGA" or x+y+z == "AGG":
        print("Arginine (Arg)")
    elif x+y+z == "GUU" or x+y+z == "GUC" or x+y+z == "GUA" or x+y+z == "GUG":
        print("Valine (Val)")   
    elif x+y+z == "GCU" or x+y+z == "GCC" or x+y+z == "GCA" or x+y+z == "GCG":
        print("Alanine (Ala)")
    elif x+y+z == "GAU" or x+y+z == "GAC":
        print("Aspartic Acid (Asp)")
    elif x+y+z == "GAA" or x+y+z == "GAG":
        print("Glutamic Acid (Glu)")
    elif x+y+z == "GGU" or x+y+z == "GGC" or x+y+z == "GGA" or x+y+z == "GGG":
        print("Glycine (Gly)")
    else:
        print("Invalid codon:", x+y+z)



#MY FIRST ACTUAL PROJECT!!!!!!
#THE IDEA BEHIND THIS IS TO TAKE AN MRNA SEQUENCE AND TRANSLATE IT INTO IT'S CONSTITUENT AMINO ACIDS.KINDDA LIKE HOW THE RIBOSME ALONG WITH THE TRNA TRANSLATES RNA TO RPOTEIN!!!
# FIRST I MADE A DICTIONARY OF ALL THE CODONS AND THEIR RESPECTIVE AMINO ACIDS.( GEMINI HELPED CAUSE IT'S A PAIN TO WRITE EM' ALL OUT BY HAND:/)
#THEN I WROTE THE CODE USING A FOR LOOP AND IF AND ELIF STATEMENTS WHICH I JUST LEARNT ABOUT TODAY!!!(24/06/2026)
#AFTER SOME FURIOUS TYPING AND A FEW MAJOR LEAGUE GLITCHES I GOT IT!TOOK THE WHOLE EVENING BUT THE EFFORT WAS WORTH ITTT!!!!!!!!!!!!!!!!
#THOUGH I CAN'T HELP BUT WONDER IF THERE WAS A MORE EFFIECIENT WAY TO WRITE THE CODE ? SRSLY THERE ARE IF AND ELIF TEXT BLOCKS SWIRLING OVER MY HEAD RN :(
# ALSO I TRIED IT ON AN ACTUAL MRNA SEQUENCE BUT IT SHOWED A LOT OF INVALID CODONS. HOW IS THIS POSSIBLE!? I GOT IT FROM THE NCBI DATABASE HOW??
# I MADE THE MOST CLICHE MISTAKE OF ALL TIME! FORGOT TO REPLACE T'S WITH U'S IN THE MRNA SEQUENCE! SILLY ME!
#MADE SOME ADJUSTMENTS AND IT WORKED LIKE MAGIC! IT WOOOOORKED!!!!!!!!!!!










