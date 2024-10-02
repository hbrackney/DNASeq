class DNASeq:
    """_summary_
    """

    def __init__(self, dna_seq: str) -> None:
        self.is_dna_sequence(dna_seq)
        self.sequence = dna_seq.lower()

    def is_dna_sequence(self, presumed_dna: str) -> None:
        """_summary_

        Args:
            presumed_dna (str): _description_
        """
        if all(char in 'actg' for char in presumed_dna.lower()) is not True:
            raise ValueError("Please input valid DNA sequence")

# Test Cases
# x = DNASeq('actgatcg')
# y = DNASeq('latcagat')
# print(x.sequence)
