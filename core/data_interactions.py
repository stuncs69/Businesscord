import json
def get_country(code):
    with open(f"data/countries/{code}") as f:
        data = json.load(f)
    return data