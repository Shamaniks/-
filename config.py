tdb_file = "forms.json"

REGEXES = {
    "email": r"^[\w\.-]+@[\w\.-]+\.\w+$",
    "phone": r"^\+7 \d{3} \d{3} \d{2} \d{2}$",
    "date": r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})$|^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"
}

NFT = { # New Form Template
    "start": "{\n",
    "end": "\n}\n",
    "row_start": "\t",
    "row_end" : "",
    "field_type_separator": ": ",
    "row_separator": ",\n"
}
