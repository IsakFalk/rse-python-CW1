

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
