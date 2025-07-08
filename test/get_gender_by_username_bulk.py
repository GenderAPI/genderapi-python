from genderapi import GenderAPI

api = GenderAPI("YOUR_API_KEY")

result = api.get_gender_by_username_bulk([
    {"username": "johnblack", "country": "US", "id": "u001"},
    {"username": "maria2025", "country": "DE", "id": "u002"}
])

print(result)