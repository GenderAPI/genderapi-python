from genderapi import GenderAPI

api = GenderAPI("YOUR_API_KEY")

result = api.get_gender_by_username(
    username="michael_dev",
    country="US",
    askToAI=False,
    forceToGenderize=False
)

print("Result for username 'michael_dev':")
print(result)
