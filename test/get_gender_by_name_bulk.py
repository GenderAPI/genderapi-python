from genderapi import GenderAPI

api = GenderAPI("YOUR_API_KEY")

result = api.get_gender_by_name_bulk([
    {"name": "Andrea", "country": "DE", "id": "123"},
    {"name": "andrea", "country": "IT", "id": "456"},
    {"name": "james", "country": "US", "id": "789"}
])

print(result)
