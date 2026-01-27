def to_rna(dna_strand):
    matchings = {'A':'U','T':'A','C':'G','G':'C'}
    transcribed = []
    for nucleotide in dna_strand:
        nucleotide_transcription = matchings[nucleotide]
        transcribed.append(nucleotide_transcription)
    return ''.join(transcribed)
        
        
        
