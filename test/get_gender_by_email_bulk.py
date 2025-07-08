from genderapi import GenderAPI

api = GenderAPI("YOUR_API_KEY")

result = api.get_gender_by_email_bulk([
    {"email": "john@example.com", "country": "US", "id": "abc123"},
    {"email": "maria@domain.de", "country": "DE", "id": "def456"}
])

print(result)
