from active_cookie import parse

expected_output = [
        ('cookie01', '2026-02-10'),
        ('cookie02', '2026-02-10'),
        ('cookie01', '2026-02-10'),
        ('cookie02', '2026-02-05'),
        ('cookie03', '2026-02-04')
    ]

# test if cookie and date are fetched from each line as expected
def test_cookie_and_date(temp_file):
    with open(temp_file) as file:
        for line, (expt_cookie, expt_date) in zip(file, expected_output):
            assert parse.cookie_and_date(line) == (expt_cookie, expt_date)

# test if the most active cookie is returned for given date
def test_most_active_cookies_single_result(temp_file):
    assert parse.most_active_cookies(temp_file, '2026-02-10') == {'cookie01'}

# test if active cookie is returned for other dates
def test_most_active_cookies_other_dates(temp_file):
    assert parse.most_active_cookies(temp_file, '2026-02-05') == {'cookie02'}
    assert parse.most_active_cookies(temp_file, '2026-02-04') == {'cookie03'}