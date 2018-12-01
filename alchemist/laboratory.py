import random


class Laboratory:
    """Laboratory class for simulating wizardry on the standardised 2-shelf wizard lab"""

    def __init__(self, lower, upper):
        """Initialise laboratory, with lab_shelves

        lab_shelves is a dictionary of the lower and upper shelves
        specified as lists of strings representing the substances of
        this laboratory and its lower and upper shelves.

        :param lower: list of strings specifying substances on lower shelf in lab
        :param upper: list of strings specifying substances on upper shelf in lab
        """
        self.lab_shelves = dict(lower=lower, upper=upper)

    @staticmethod
    def can_react(substance1, substance2):
        """Checks if two substances can react with eachother

        Two substances, substance1 and substance2 are able to react if they
        are such they are the anti-substances of each other. What this means is that
        either the string of substance1 is the concatenation of 'anti' and the string of
        subtance2 or the other way around.

        :param substance1: string specifying a substance
        :param substance2: string specifying another substance

        :return: boolean specifying if the two substances can react or not
        """
        return (substance1 == "anti" + substance2) or (substance2 == "anti" + substance1)

    @staticmethod
    def update_shelves(shelf_lower, shelf_upper, substance_lower, substance_upper_index):
        """Update the shelves by removing the substances reacting

        Removes the substances from the upper and lower shelves if a reaction
        takes place. Note that this does not check itself if the substances can
        react, but will remove them regardless of what is passed in.

        :param shelf_lower: list of strings specifying substances on lower shelf in lab
        :param shelf_upper: list of strings specifying substances on lower shelf in lab
        :param substance_lower: string specifying a substance on lower shelf
        :param substance_upper_index: integer specifying the index of a substance on upper shelf (0-indexed)

        :return: tuple of two lists of the new updated lower and upper shelves in the lab
        """
        index_lower = shelf_lower.index(substance_lower)
        shelf_lower = shelf_lower[:index_lower] + shelf_lower[index_lower+1:]
        shelf_upper = shelf_upper[:substance_upper_index] + \
            shelf_upper[substance_upper_index+1:]
        return shelf_lower, shelf_upper

    @staticmethod
    def do_a_reaction(shelf_lower, shelf_upper):
        """Carry out a reaction using the given lower and upper shelves

        Going through each substance in the lower shelf in order, check if
        there are any substances in the upper shelf that can react with the
        currently chosen substance from the lower shelf. If this does not
        exist, continue to the next substance, if there are potential reactants
        in the upper shelf, pick one uniformly random from this set, carry out
        the reaction and return the updated shelves by removing the reactants.

        Note that if none of the substances in the lower shelf can react with
        any of the substances in the upper shelf, the shelves will stay the
        same and no reaction will take place (e.g. this method becomes
        idempotent in this case).

        :param shelf_lower: list of strings of the substances in the lower shelf
        :param shelf_upper: list of strings of the substances in the upper shelf

        :return: tuple of two lists of the lower and upper shelves after trying to carry out a reaction
        """
        for substance_lower in shelf_lower:
            possible_targets = [i for i, target in enumerate(
                shelf_upper) if Laboratory.can_react(substance_lower, target)]
            if not possible_targets:
                continue
            else:
                substance_upper_index = random.choice(possible_targets)
                return Laboratory.update_shelves(shelf_lower, shelf_upper, substance_lower, substance_upper_index)
        return shelf_lower, shelf_upper

    def run_full_experiment(self):
        """Run a full experiment on the current laboratory

        Following the wizard specification for carrying out lab work on the
        standardised 2-shelf wizard lab this function simulates a run. At each
        reaction attempt, it goes through the substances in the lower shelf
        from left to right, when it finds a substance which can react with one
        or more substances on the upper shelf it uniformly randomly picks one
        of these substances to react with and removes the reactants.

        It does this until no more reactions can take place at which point it
        terminates, printing the total number of reactions and return the final
        lower and upper shelves.

        :return: lower_shelf, upper_shelf, the final shelves after running the experiment session
        """
        # TODO: It is probably much easier to have the shelves changed in place
        # and have the return of do_a_reaction return something like
        # reaction_took_place which will be a boolean
        count = 0
        ended = False
        while not ended:
            shelf1_new, shelf2_new = Laboratory.do_a_reaction(shelf1, shelf2)
            if shelf1_new != shelf1:
                count += 1
            ended = (shelf1_new == shelf1) and (shelf2_new == shelf2)
            shelf1, shelf2 = shelf1_new, shelf2_new
        print("Total number of reactions: {}".format(count))
        return shelf1, shelf2
