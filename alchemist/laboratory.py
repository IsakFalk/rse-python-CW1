

class Laboratory:

    def __init__(self, lower, upper):
        """Initialise laboratory, with lab_shelves

        lab_shelves is a dictionary of the lower and upper shelves
        specified as lists of strings representing the substances of
        this laboratory and its lower and upper shelves.

        :param lower: list of strings specifying substances on lower shelf in lab
        :param upper: list of strings specifying substances on upper shelf in lab
        """
        self.lab_shelves = dict(lower=lower, upper=upper)

    def can_react(self, substance1, substance2):
        """Checks if two substances can react with eachother

        Two substances, substance1 and substance2 are able to react if they
        are such they are the anti-substances of each other. What this means is that
        either the string of substance1 is the concatenation of 'anti' and the string of
        subtance2 or the other way around.

        :param substance1: string specifying a substance
        :param substance2: string specifying another substance

        :return: boolean specifying if the two substances can react or not"""
        return (substance1 == "anti" + substance2) or (substance2 == "anti" + substance1)
