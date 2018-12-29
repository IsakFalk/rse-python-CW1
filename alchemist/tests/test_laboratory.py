"""Tests of the alchemist package"""
import os

import pytest
import yaml
from pytest import raises

from ..laboratory import Laboratory


# run_full_experiment tests
def test_full_experiment_normal_usage():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["full_experiment_normal_usage"]
    lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])
    lower, upper, count = lab.run_full_experiment()
    assert (
        lower == fixture["lower_final"]
        and upper == fixture["upper_final"]
        and count == fixture["num_reactions"]
    )


def test_full_experiment_empty_upper():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["full_experiment_empty_upper"]
    lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])
    lower, upper, count = lab.run_full_experiment()
    assert (
        lower == fixture["lower_final"]
        and upper == fixture["upper_final"]
        and count == fixture["num_reactions"]
    )


def test_full_experiment_empty_lower():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["full_experiment_empty_lower"]
    lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])
    lower, upper, count = lab.run_full_experiment()
    assert (
        lower == fixture["lower_final"]
        and upper == fixture["upper_final"]
        and count == fixture["num_reactions"]
    )


def test_full_experiment_empty_upper_lower():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["full_experiment_empty_upper_lower"]
    lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])
    lower, upper, count = lab.run_full_experiment()
    assert (
        lower == fixture["lower_final"]
        and upper == fixture["upper_final"]
        and count == fixture["num_reactions"]
    )


def test_full_experiment_empty_string_upper():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["full_experiment_empty_string_upper"]
    lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])
    lower, upper, count = lab.run_full_experiment()
    assert (
        lower == fixture["lower_final"]
        and upper == fixture["upper_final"]
        and count == fixture["num_reactions"]
    )


def test_full_experiment_empty_string_lower():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["full_experiment_empty_string_lower"]
    lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])
    lower, upper, count = lab.run_full_experiment()
    assert (
        lower == fixture["lower_final"]
        and upper == fixture["upper_final"]
        and count == fixture["num_reactions"]
    )


def test_full_experiment_empty_string_upper_lower():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["full_experiment_empty_string_upper_lower"]
    lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])
    lower, upper, count = lab.run_full_experiment()
    assert (
        lower == fixture["lower_final"]
        and upper == fixture["upper_final"]
        and count == fixture["num_reactions"]
    )


def test_full_experiment_empty_string_upper_lower():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["full_experiment_empty_string_upper_lower"]
    lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])
    lower, upper, count = lab.run_full_experiment()
    assert (
        lower == fixture["lower_final"]
        and upper == fixture["upper_final"]
        and count == fixture["num_reactions"]
    )


def test_negative_full_experiment_wrong_input_types_upper():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["negative_full_experiment_wrong_input_types_upper"]
    with raises(TypeError) as exception:
        lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])


def test_negative_full_experiment_wrong_input_types_lower():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["negative_full_experiment_wrong_input_types_lower"]
    with raises(TypeError) as exception:
        lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])


def test_negative_full_experiment_wrong_input_shelves_lower():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["negative_full_experiment_wrong_input_shelves_lower"]
    with raises(TypeError) as exception:
        lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])


def test_negative_full_experiment_wrong_input_shelves_upper():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["negative_full_experiment_wrong_input_shelves_upper"]
    with raises(TypeError) as exception:
        lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])


# update_shelves
def test_update_shelves_reaction():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["update_shelves_reaction"]
    lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])
    lab.update_shelves(fixture["substance"], fixture["index"])
    assert (
        lab.shelves["lower"] == fixture["lower_answer"]
        and lab.shelves["upper"] == fixture["upper_answer"]
    )


def test_negative_update_shelves_no_such_substance():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["negative_update_shelves_no_such_substance"]
    lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])
    with raises(ValueError) as exception:
        lab.update_shelves(fixture["substance"], fixture["index"])


def test_negative_update_shelves_index_out_of_bounds():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["negative_update_shelves_index_out_of_bounds"]
    lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])
    with raises(IndexError) as exception:
        lab.update_shelves(fixture["substance"], fixture["index"])


# can_react
def test_can_react_successful():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["can_react_successful"]
    lab = Laboratory()
    assert lab.can_react(fixture["substance1"], fixture["substance2"])


def test_can_react_successful_flipped():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["can_react_successful_flipped"]
    lab = Laboratory()
    assert lab.can_react(fixture["substance1"], fixture["substance2"])


def test_can_react_not_successful():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["can_react_not_successful"]
    lab = Laboratory()
    assert not lab.can_react(fixture["substance1"], fixture["substance2"])


def test_can_react_empty_string_successful():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["can_react_empty_string_successful"]
    lab = Laboratory()
    assert lab.can_react(fixture["substance1"], fixture["substance2"])


def test_can_react_antianti_successful():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["can_react_antianti_successful"]
    lab = Laboratory()
    assert lab.can_react(fixture["substance1"], fixture["substance2"])


def test_negative_can_react_wrong_input_type_substance1():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["negative_can_react_wrong_input_type_substance1"]
    lab = Laboratory()
    with raises(TypeError) as exception:
        lab.can_react(fixture["substance1"], fixture["substance2"])


def test_negative_can_react_wrong_input_type_substance2():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["negative_can_react_wrong_input_type_substance2"]
    lab = Laboratory()
    with raises(TypeError) as exception:
        lab.can_react(fixture["substance1"], fixture["substance2"])


# do_a_reaction
def test_do_a_reaction_random_sampling():
    with open(
        os.path.join(os.path.dirname(__file__), "fixtures.yml"), "r"
    ) as fixture_file:
        fixtures = yaml.load(fixture_file)
    fixture = fixtures["do_a_reaction_random_sampling"]
    lab = Laboratory(lower=fixture["lower"], upper=fixture["upper"])
    lab.do_a_reaction()
    assert lab.shelves["lower"] == fixture["lower_final"] and (
        lab.shelves["upper"] == fixture["upper_final_1"]
        or lab.shelves["upper"] == fixture["upper_final_2"]
    )
