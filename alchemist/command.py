import argparse
import yaml

from alchemist.laboratory import Laboratory

def process():
    parser = argparse.ArgumentParser(description="Run experiment on a wizardry 2-shelf laboratory")
    parser.add_argument("shelves", default="laboratory.yaml", type=str, help="YAML file specifying the laboratory shelves")
    parser.add_argument("--reactions", "-r", action="store_true", help="print the number of reactions that occurred during experiment")
    args = parser.parse_args()

    # Perform experiment using yaml file as input
    with open(args.shelves, 'r') as f:
        lab_shelves = yaml.load(f)
    lab = Laboratory(lab_shelves['lower'], lab_shelves['upper'])
    num_reactions, final_lower_shelf, final_upper_shelf = lab.run_full_experiment()

    if args.reactions:
        print(num_reactions)
    else:
        print("lower: {}\nupper: {}".format(final_lower_shelf, final_upper_shelf))
