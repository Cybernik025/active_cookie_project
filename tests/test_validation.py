import pytest
from active_cookie.validation import is_valid_arguments

valid_dates_in_file = ['2026-02-10', '2026-02-05', '2026-02-04']
invalid_test_date_formats = ['2026/02/10', '2026-01-2', '01-12-2019']
valid_dates_not_in_file = ['2026-01-02', '2019-11-01', '2020-03-25']

@pytest.fixture
def temp_file(tmp_path):
    file_path = str(tmp_path) + "/cookie_log.csv"
    with open(file_path, "w") as file:
        file.write("\n".join(["cookie01,2026-02-10T16:19:00+00:00",
                   "cookie02,2026-02-10T12:20:00+00:00",
                   "cookie01,2026-02-10T00:09:00+00:00",
                   "cookie02,2026-02-05T15:19:00+00:00",
                   "cookie03,2026-02-04T22:19:00+00:00"]))
    return file_path

# test valid file + valid date
@pytest.mark.parametrize('test_date', valid_dates_in_file)
def test_valid_file_valid_date(temp_file, test_date):
    assert is_valid_arguments(temp_file, test_date)

# test valid file + invalid date formats
@pytest.mark.parametrize('test_date', invalid_test_date_formats)
def test_valid_file_invalid_date_format(temp_file, test_date):
    assert not is_valid_arguments(temp_file, test_date)

# test valid file + valid date format but not in file
@pytest.mark.parametrize('test_date', valid_dates_not_in_file)
def test_valid_file_valid_date_not_in_file(temp_file, test_date):
    assert not is_valid_arguments(temp_file, test_date)

# test invalid file + valid date
@pytest.mark.parametrize('test_date', valid_dates_in_file)
def test_invalid_file_valid_date(test_date):
    with pytest.raises(FileNotFoundError):
        is_valid_arguments("", test_date)

# test invalid file + invalid date formats
@pytest.mark.parametrize('test_date', invalid_test_date_formats)
def test_invalid_file_invalid_date(test_date):
    with pytest.raises(FileNotFoundError):
        is_valid_arguments("", test_date)

# test invalid file + valid dates not in file
@pytest.mark.parametrize('test_date', valid_dates_not_in_file)
def test_invalid_file_valid_date_not_in_file(test_date):
    with pytest.raises(FileNotFoundError):
        is_valid_arguments("", test_date)