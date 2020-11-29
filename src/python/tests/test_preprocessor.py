import sys
sys.path.insert(0, 'src')
import pytest
import os.path
import pandas as pd
from preprocessing import preprocessor as pp
from config import config
#os.path.isfile(fname)


@pytest.fixture()
def get_data():
    return pd.read_csv('tests/resources/sample_df.csv')


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """Cleanup testing files once we are finished."""
    def remove_test_files(test_encodings_path='tests/encodings/'):
        files = os.listdir(test_encodings_path)
        for col in config.CAT_VARS:
            if f"{col}_encoder.npy" in files:
                os.remove(f"{test_encodings_path}{col}_encoder.npy")
    request.addfinalizer(remove_test_files)


def test_fit_and_save_encodings(get_data, test_encodings_path='tests/encodings'):
    pp.fit_and_save_encodings(get_data, cat_cols=config.CAT_VARS, encodings_path=test_encodings_path)
    for var in config.CAT_VARS:
        assert os.path.isfile(f"{test_encodings_path}/{var}_encoder.npy"), "Encodings not found"


def test_load_and_transform_encoder():
    pass


def test_load_and_invert_transform_encoder():
    pass


def test_convert_empty_lines_to_na():
    pass


def test_remove_na():
    pass


def test_encode_target():
    pass
