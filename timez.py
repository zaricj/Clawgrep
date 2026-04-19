from datetime import date, datetime

today = datetime.now()

formatted = today.strftime("%d.%m.%Y %H:%M:%S")

weird_date = "2026-03-26T08:53:31,935"

ident = datetime.fromisoformat(weird_date)

print(formatted)
print(ident.strftime("%d.%m.%Y %H:%M:%S"))

test_dict = {
    "Name": "Joe",
    "Age": "20",
    "Location": "Berlin",
    "Occupation": "Contract Assassin"
}

for key in test_dict:
    print(f"Key: {key}")
    print(f"Value: {test_dict[key]}")
