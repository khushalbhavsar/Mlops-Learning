import re


def show(title: str, value) -> None:
    print(f"\n{title}")
    print(value)


def basic_functions_demo() -> None:
    text = "I love Python. Python is easy."
    show("re.match('Python', text):", re.match("Python", text))  # Output: None

    show("re.search('Python', text):", re.search("Python", text))  # Output: <re.Match object; span=(7, 13), match='Python'>

    show("re.findall('Python', text):", re.findall("Python", text))  # Output: ['Python', 'Python']

    show(
        "re.finditer('Python', text) spans:",
        [(m.start(), m.end()) for m in re.finditer("Python", text)],
    )  # Output: [(7, 13), (15, 21)]

    show("re.sub('easy', 'powerful', text):", re.sub("easy", "powerful", text))  # Output: I love Python. Python is powerful.

    show(
        "re.split('[,; ]', 'apple,banana;orange mango'):",
        re.split("[,; ]", "apple,banana;orange mango"),
    )  # Output: ['apple', 'banana', 'orange', 'mango']

    show("re.fullmatch(r'\\d+', '12345'):", bool(re.fullmatch(r"\d+", "12345")))  # Output: True



def syntax_demo() -> None:
    show("Dot . -> re.findall('c.t', 'cat cut cot'):", re.findall("c.t", "cat cut cot"))  # Output: ['cat', 'cut', 'cot']

    show("Caret ^ -> re.match('^Hello', 'Hello World'):", bool(re.match("^Hello", "Hello World")))  # Output: True

    show("Dollar $ -> re.search('World$', 'Hello World'):", bool(re.search("World$", "Hello World")))  # Output: True

    show("Star * -> re.findall('ab*', 'a ab abb abbb'):", re.findall("ab*", "a ab abb abbb"))  # Output: ['a', 'ab', 'abb', 'abbb']

    show("Plus + -> re.findall('ab+', 'a ab abb abbb'):", re.findall("ab+", "a ab abb abbb"))  # Output: ['ab', 'abb', 'abbb']

    show("Question ? -> re.findall('colou?r', 'color colour'):", re.findall("colou?r", "color colour"))  # Output: ['color', 'colour']

    show("Curly {3} -> re.findall(r'\\d{3}', '1234 567 89'):", re.findall(r"\d{3}", "1234 567 89"))  # Output: ['123', '567']



def classes_and_sets_demo() -> None:
    show(r"\d:", re.findall(r"\d", "A1B2C3"))  # Output: ['1', '2', '3']

    show(r"\D:", re.findall(r"\D", "A1B2"))  # Output: ['A', 'B']

    show(r"\w:", re.findall(r"\w", "A_12"))  # Output: ['A', '_', '1', '2']

    show(r"\W:", re.findall(r"\W", "A@12"))  # Output: ['@']

    show(r"\s:", re.findall(r"\s", "A B\tC\nD"))  # Output: [' ', '\t', '\n']

    show(r"\S:", re.findall(r"\S", "A B\tC\nD"))  # Output: ['A', 'B', 'C', 'D']

    show("[abc] in 'apple banana cat':", re.findall("[abc]", "apple banana cat"))  # Output: ['a', 'b', 'a', 'a', 'a', 'c', 'a']

    show("[^0-9] in 'A1B2':", re.findall(r"[^0-9]", "A1B2"))  # Output: ['A', 'B']



def groups_demo() -> None:
    text = "2026-08-05"
    match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
    if match:
        show("Grouped date parts:", (match.group(1), match.group(2), match.group(3)))  # Output: ('2026', '08', '05')


    named = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})", "2026-08")
    if named:
        show("Named group 'year':", named.group("year"))  # Output: 2026



def flags_and_compile_demo() -> None:
    show("OR operator cat|dog:", re.findall("cat|dog", "cat dog lion"))  # Output: ['cat', 'dog']

    show(
        "IGNORECASE for 'python' in 'Python':",
        re.findall("python", "Python", re.IGNORECASE),
    )  # Output: ['Python']

    multiline_text = "start\nmiddle\nend"
    show(
        "MULTILINE for '^middle$':",
        re.findall(r"^middle$", multiline_text, re.MULTILINE),
    )  # Output: ['middle']

    dotall_text = "line1\nline2"
    show("DOTALL for 'line1.*line2':", bool(re.search(r"line1.*line2", dotall_text, re.DOTALL)))  # Output: True

    compiled = re.compile(r"\d+")
    show("Compiled regex on '123 abc 456':", compiled.findall("123 abc 456"))  # Output: ['123', '456']



def validation_and_extraction_demo() -> None:
    email = "user@gmail.com"
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    show("Email valid:", bool(re.fullmatch(email_pattern, email)))  # Output: True


    number = "9876543210"
    mobile_pattern = r"^[6-9]\d{9}$"
    show("Mobile valid:", bool(re.fullmatch(mobile_pattern, number)))  # Output: True


    password = "Pass@123"
    password_pattern = (
        r"^(?=.*[A-Z])"
        r"(?=.*[a-z])"
        r"(?=.*\d)"
        r"(?=.*[@$!%*?&])"
        r"[A-Za-z\d@$!%*?&]{8,}$"
    )
    show("Password valid:", bool(re.fullmatch(password_pattern, password)))  # Output: True


    url_text = "Visit https://example.com or http://test.com"
    show("Extracted URLs:", re.findall(r"https?://\S+", url_text))  # Output: ['https://example.com', 'http://test.com']


    ip_text = "Server IP: 192.168.1.100"
    show("Extracted IPs:", re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", ip_text))  # Output: ['192.168.1.100']


    log = "CPU=85 Memory=72 Disk=90"
    show("Numbers from log:", re.findall(r"\d+", log))  # Output: ['85', '72', '90']


    logs = """
INFO Server started
ERROR Database failed
INFO Request received
ERROR Disk full
"""
    show("ERROR lines:", re.findall(r"ERROR.*", logs))  # Output: ['ERROR Database failed', 'ERROR Disk full']


    pods = """
nginx-54df7
redis-1ab2
mongo-7788
"""
    show("Pod names:", re.findall(r"\w+-\w+", pods))  # Output: ['nginx-54df7', 'redis-1ab2', 'mongo-7788']



def main() -> None:
    print("=== Python Regex Practice ===")
    basic_functions_demo()
    syntax_demo()
    classes_and_sets_demo()
    groups_demo()
    flags_and_compile_demo()
    validation_and_extraction_demo()


if __name__ == "__main__":
    main()

