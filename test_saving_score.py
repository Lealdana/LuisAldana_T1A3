# Import functions from main module
from main import saving_score, user_name, score
import pytest

# Function to test the Saving_score function


def test_saving_score(tmp_path):
    filename = tmp_path / "test_scores.csv"
    saving_score(filename)

    assert filename.exists()
    with open(filename) as f:
        lines = f.readlines()
        assert len(lines) == 2
        assert lines[0].strip() == "name,score"
        assert lines[1].strip() == f"{user_name},{score}"
