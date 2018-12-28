"""
Class representing a standardised 2-shelf wizard lab
with methods for performing experiments
"""
import random


class Laboratory:
    """Laboratory class for simulating wizardry on the standard. 2-shelf lab"""

    def __init__(self, lower=[], upper=[]):
        """Initialise laboratory, with shelves

        shelves is a dictionary of the lower and upper shelves
        specified as lists of strings representing the substances of
        this laboratory and its lower and upper shelves.

        :param lower: list of strings specifying substances on lower shelf
        :param upper: list of strings specifying substances on upper shelf
        """
        # Check for faulty input
        if not isinstance(lower, list) or not isinstance(upper, list):
            raise TypeError(
                "The lower and upper shelves need to be of type list."
            )
        if (lower != [] and any([not isinstance(x, str) for x in lower])) or (
            upper != [] and any([not isinstance(x, str) for x in upper])
        ):
            raise TypeError(
                "The substances of the shelves need to be strings."
            )
        self.shelves = dict(lower=lower, upper=upper)

    def update_shelves(self, substance_lower, substance_upper_index):
        """Update the shelves by removing the substances reacting

        Removes the substances from the upper and lower shelves if a reaction
        takes place. Note that this does not check itself if the substances can
        react, but will remove them regardless of what is passed in.
        :param substance_lower: string specifying a substance on lower shelf
        :param substance_upper_index: integer specifying the index of a
        substance on upper shelf (0-indexed)

        :return: tuple of two lists of the new updated lower and upper shelves
        in the lab
        """
        if substance_lower not in self.shelves["lower"]:
            raise ValueError(
                "The substance {} is not the lower shelf.".format(
                    substance_lower
                )
            )
        if substance_upper_index < 0 or substance_upper_index >= len(
            self.shelves["upper"]
        ):
            raise IndexError(
                "The index {} is out of range.".format(substance_upper_index)
            )
        index_lower = self.shelves["lower"].index(substance_lower)
        self.shelves["lower"] = (
            self.shelves["lower"][:index_lower]
            + self.shelves["lower"][index_lower + 1:]
        )
        self.shelves["upper"] = (
            self.shelves["upper"][:substance_upper_index]
            + self.shelves["upper"][substance_upper_index + 1:]
        )

    def can_react(self, substance1, substance2):
        """Checks if two substances can react with eachother

        Two substances, substance1 and substance2 are able to react if they
        are such they are the anti-substances of each other. What this means
        is that either the string of substance1 is the concatenation of 'anti'
        and the string of subtance2 or the other way around.

        :param substance1: string specifying a substance
        :param substance2: string specifying another substance

        :return: boolean specifying if the two substances can react or not
        """
        if not isinstance(substance1, str) or not isinstance(substance2, str):
            raise TypeError("The passed substances need to be strings.")
        return (substance1 == "anti" + substance2) or (
            substance2 == "anti" + substance1
        )

    def do_a_reaction(self):
        """Carry out a reaction using the given lower and upper shelves

        Going through each substance in the lower shelf in order, check if
        there are any substances in the upper shelf that can react with the
        currently chosen substance from the lower shelf. If this does not
        exist, continue to the next substance, if there are potential
        reactants in the upper shelf, pick one uniformly random from this set,
        carry out the reaction and return the updated shelves by removing the
        reactants.

        Note that if none of the substances in the lower shelf can react with
        any of the substances in the upper shelf, the shelves will stay the
        same and no reaction will take place (e.g. this method becomes
        idempotent in this case).

        :return reaction_occurred: boolean specifying if a reaction occurred
        """
        reaction_occurred = False
        for substance_lower in self.shelves["lower"]:
            possible_targets = [
                i
                for i, target in enumerate(self.shelves["upper"])
                if self.can_react(substance_lower, target)
            ]
            if not possible_targets:
                continue
            else:
                substance_upper_index = random.choice(possible_targets)
                self.update_shelves(substance_lower, substance_upper_index)
                reaction_occurred = True
                return reaction_occurred
        return reaction_occurred

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

        :return: (lower_shelf, upper_shelf, count) the final shelves after
        running the experiment session and total number of reactions taken
        place

        """
        count = 0
        ended = False
        while not ended:
            reaction_occurred = self.do_a_reaction()
            if reaction_occurred:
                count += 1
            else:
                # If no reaction occurred, the experiment is done
                ended = True
        return self.shelves["lower"], self.shelves["upper"], count
