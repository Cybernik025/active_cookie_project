def most_active_cookies(file_name : str, date : str) -> list[str]:
    cookie_dict = {}
    max_cookies = set()
    max_count = 0

    with open(file_name, "r") as file:
        for line in file:
            cookie, cookie_date = cookie_and_date(line)

            if date == cookie_date:
                cookie_dict[cookie] = cookie_dict.get(cookie, 0) + 1
                count = cookie_dict[cookie]

                if count > max_count:
                    max_count = count
                    max_cookies = {cookie}
                elif count == max_count:
                    max_cookies.add(cookie)  

    return max_cookies

def cookie_and_date(line : str) -> tuple[str, str]:
    log_list = line.strip().split(",")
    cookie = log_list[0]
    time_stamp = log_list[1].split("T")
    cookie_date = time_stamp[0]

    return cookie, cookie_date