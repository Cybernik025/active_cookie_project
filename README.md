# MOST ACTIVE COOKIE(s)
A Python command line program that processes a log file and returns the most active cookie(s) for a specific day

## Features
* Process cookie log file in CSV format
* Find the most active cookie(s) for a given date
* Handle multiple cookies with the same frequency of occurence
* Logs program events, errors and debug information to a log file
* Easy to maintain and extend

## Tech Stack
* Python 3 - Core language
* argparse - library for parsing and building the CLI
* logging - library for logging program events, info and errors
* pytest - Unit testing framework

## Setup
1. Clone the repository
```
git clone https://github.com/Cybernik025/active_cookie_project.git
cd active_cookie_project
```

2. Ensure Python 3+ is installed
```
python3 --version
```

3. Install the package in development mode
```
pip install -e .
```

4. Install test dependencies
```
pip install pytest
```

## Usage
* Run the program using either method:

**Method 1: Using python -m**
```
python3 -m active_cookie.cli -f cookie_log.csv -d 2018-12-09
```

**Method 2: Using the installed command -m**
```
active-cookie -f cookie_log.csv -d 2018-12-09
```

* Output: 
```AtY0laUfhglK3lC7```
* If multiple cookies meet the required criteria, each is returned and printed on separate lines for that given date

## Testing
Run all tests with
```
pytest tests/
```
* Validates ```most_active_cookies``` logic
* Validates ```cookie_and_date``` parsing
* Ensures input validation works correctly

## Logging
* Logs are written to 'logs/log.log' in the project directory
* Includes log level and messages
* Supports INFO, WARNING and ERROR messages

## Assumptions
* Input CSV is sorted by timestamp (most recent first)
* Date argument is a valid date in UTC timezone
* There is enough memory to store entire file's contents

