import re
import sys

from abstract_db import AbstractDatabase
from tiny_db import TinyDatabase
from config import REGEXES, NFT

def get_field_type(value: str) -> str:
    for field_type, regex in REGEXES.items():
        if re.match(regex, value):
            return field_type
    return "text"

def split_arg(arg: str) -> tuple[str, str]:
    key, value = arg.split('=')
    return (key[2:], value)

def parse_args(args: list[str]) -> dict[str, str]:
    return {key: get_field_type(value) for key, value in map(split_arg, args)}

def get_forms(fields: dict[str, str], db: AbstractDatabase) -> list[str]:
    return db.find_templates(fields)

def response_on_forms(forms: list[str]) -> None:
    print('\n'.join(forms))

def response_on_empty(fields: dict[str, str]) -> None:
    print_form = lambda x: print(NFT[x], end="")
    def print_field_name(name: str, field: str, sep: bool) -> None:
        print_form("row_start")
        print(name, end="")
        print_form("field_type_separator")
        print(fields[name], end="")
        if sep: print_form("row_separator")
        
    print_form("start")
    field_names = list(fields.keys())
    [print_field_name(name, fields[name], True) for name in field_names[:-1]]
    name = field_names[-1]
    print_field_name(name, fields[name], False)
    print_form("end")

def main() -> int:
    if len(sys.argv) == 1:
        print("Применение: python app.py [<имя поля>=<значение>]*")
        return 0

    flags = list(filter(lambda x: x.startswith("--"), sys.argv))
    field_type_dict = parse_args(flags)
    forms = get_forms(field_type_dict, TinyDatabase())
    response_on_forms(forms) if forms else response_on_empty(field_type_dict)
    return 0

if __name__ == "__main__":
    exit(main())

