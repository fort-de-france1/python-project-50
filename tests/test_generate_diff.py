from pathlib import Path
import pytest
from diff.generate_diff import generate_diff
from .result_json import result_gen_diff


@pytest.fixture()
def data():
    f1_json = Path().cwd() / "tests" / 'fixtures' / 'file1.json'
    f2_json = Path().cwd() / "tests" /'fixtures' / 'file2.json'
    return {
        "f1_json": f1_json,
        "f2_json": f2_json
    }


def test_generate_diff(data):
    assert generate_diff(data["f1_json"],
                         data["f2_json"]) == result_gen_diff
