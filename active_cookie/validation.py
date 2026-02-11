def is_valid_arguments(file_name : str, date : str) -> bool:
    is_valid_date = is_valid_date_format(date)
    is_valid_file = is_valid_file_with_date(file_name, date)
    
    return is_valid_date and is_valid_file

# validate if date is in YYYY-MM-DD format
def is_valid_date_format(date : str) -> bool:
    if len(date) != 10:
        return False
    
    if date[4] != "-" or date[7] != "-":
        return False
    
    year, month, day = date[:4], date[5:7], date[8:]
    
    return year.isdigit() and month.isdigit() and day.isdigit()

# validate if file exists and if date exists in the file
def is_valid_file_with_date(file_name : str, date : str) -> bool:
    try:
        with open(file_name, "r") as file:  # check if file exists to open it
            return is_date_in_file(file.read(), date)

    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_name} not found")
    except Exception as e:
        raise Exception(f"Unknown exception while checking file '{file_name}': {e}")
    return False                

def is_date_in_file(file_contents : str, date : str) -> bool:
    return date in file_contents




    
