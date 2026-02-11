import argparse
import logging
from pathlib import Path
from active_cookie import validation
from active_cookie import parse

# Setup logging with correct location
log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "log.log"

logging.basicConfig(
    level=logging.INFO, 
    filename=str(log_file), 
    filemode="a")

def main():
    parser = argparse.ArgumentParser(description='Program to process cookie log file and return the most active cookie for a specific day')

    parser.add_argument('-f', '--file', required=True, help='Cookie log file path')
    parser.add_argument('-d', '--date', required=True, help='Date in YYYY-MM-DD format')
    
    args = parser.parse_args()
    file_name = args.file
    date = args.date
    
    logging.info(f"Processing file: {file_name} for date: {date}")

    # validates file_name and date
    try:
        if not validation.is_valid_arguments(file_name, date):
            logging.warning("Invalid date format or date not in file")
            print("No record found")
            return
    except FileNotFoundError:
        logging.error(f"File not found: {file_name}")
        print(f"Error: File '{file_name}' not found")
        return
    except Exception as e:
        logging.error(f"Validation error: {e}")
        print(f"Error: {e}")
        return

    # validation successful, ok to proceed to next task
    logging.info("Validation successful, searching for active cookies")

    # finds and returns most active cookies for the given date
    active_cookies = parse.most_active_cookies(file_name, date)

    if not active_cookies:
        logging.info(f"No cookies found for date: {date}")
    else:
        logging.info(f"Found {len(active_cookies)} most active cookies for date {date}")
    
    for cookie in active_cookies:
        print(cookie)

if __name__ == "__main__":
    main()


