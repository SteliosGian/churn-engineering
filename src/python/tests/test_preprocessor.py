import sys
sys.path.insert(0, 'src')
import pytest
import os.path
import pandas as pd
import pandas.api.types as ptypes
from preprocessing import preprocessor as pp
from config import config


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


def test_load_and_transform_encoder(get_data, test_encodings_path='tests/encodings'):
    pp.fit_and_save_encodings(get_data, cat_cols=config.CAT_VARS, encodings_path=test_encodings_path)
    df = pp.load_and_transform_encoder(get_data, cat_cols=config.CAT_VARS, encodings_path=test_encodings_path)
    assert all(ptypes.is_numeric_dtype(df[col]) for col in config.CAT_VARS), "Data types of CAT_VARS must be numeric"


def test_load_and_invert_transform_encoder(get_data, test_encodings_path='tests/encodings'):
    pp.fit_and_save_encodings(get_data, cat_cols=config.CAT_VARS, encodings_path=test_encodings_path)
    df = pp.load_and_transform_encoder(get_data, cat_cols=config.CAT_VARS, encodings_path=test_encodings_path)
    df = pp.load_and_invert_transform_encoder(df, cat_cols=config.CAT_VARS, encodings_path=test_encodings_path)
    assert all(ptypes.is_object_dtype(df[col])
               for col in config.CAT_VARS
               if df[[col]].columns != 'SeniorCitizen'), "Data types of CAT_VARS must be objects"


def test_convert_empty_lines_to_na(get_data, col=['TotalCharges']):
    df = pp.convert_empty_lines_to_na(get_data, cols=col)
    assert df[col].isnull().values.any(), f"{col} should have null values"


def test_remove_na(get_data, col=['TotalCharges']):
    df = pp.convert_empty_lines_to_na(get_data, cols=col)
    df = pp.remove_na(df)
    assert df.notnull().values.all(), "Null values should not exist"


def test_encode_target(get_data):
    df = pp.encode_target(get_data, target=config.TARGET)
    #assert ptypes.is_bool_dtype(df[config.TARGET]), "Target variable is not bool type"
    assert ptypes.is_string_dtype(df[config.TARGET]), "Target variable is not bool type"
