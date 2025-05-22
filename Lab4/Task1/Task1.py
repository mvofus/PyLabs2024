import json


def task() -> float:
    with open("input.json") as file:
        data = json.load(file)
    return round(sum(x['score'] * x['weight'] for x in data), 3)


print(task())
