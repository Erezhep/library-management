
def truncate_text(text, max_length):
    return text if len(text) <= max_length else text[:max_length - 3] + "..."


def print_on_console(datas):
        print(f"|{"id":<4}|{"title":<30}|{"author":<20}|{"year":<6}|{"status":<16}|")
        print("-" * 82)
        for data in datas:
            print(f"|{data["id"]:<4}|{truncate_text(data["title"], 30):<30}|{truncate_text(data["author"], 20):<20}|{data["year"]:<6}|{data["status"]:<16}|")