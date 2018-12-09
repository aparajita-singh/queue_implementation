import src.utils as utils


def test_standardize_date():
    assert utils.standardize_date('2017/02/10 4:59') == '2017/02/10 04:59'


def test_dequotify():
    assert utils.dequotify('""some ov"er"quote"d text"""') == 'some overquoted text'
