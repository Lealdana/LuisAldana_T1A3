from main import saving_score, user_name, score
import csv
import pytest


def test_saving_score(monkeypatch, tmp_path):
    # Define a mock input function to simulate user inputs
    user_inputs = iter(["yes"])

    def mock_input(prompt):
        nonlocal user_inputs
        return next(user_inputs)

    # Set up the test environment
    filename = tmp_path / "test_scores.csv"

    # Patch the input function with the mock input function
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the function under test
    saving_score(filename)

    # Assert that the score file has been created and contains the expected data
    assert filename.exists()
    with open(filename) as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert lines[0].strip() == "name,score"
        assert lines[1].strip() == f"{user_name},{score}"
