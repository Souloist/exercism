def to_rna(strand):

	new_strand = []
	complements = {"G":"C", "C":"G", "T":"A", "A":"U"}
	
	for nucleotide in strand:
		new_strand.append(complements[nucleotide])

	return "".join(new_strand)
