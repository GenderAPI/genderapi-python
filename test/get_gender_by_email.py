from genderapi import GenderAPI

api = GenderAPI("YOUR_API_KEY")

result = api.get_gender_by_email(
    email="michael.smith@example.com",
    country="US",
    askToAI=False
)

print("Result for email:")
print(result)
