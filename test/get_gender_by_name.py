from genderapi import GenderAPI

# Replace YOUR_API_KEY with your actual key
api = GenderAPI("YOUR_API_KEY")

# Simple test
result = api.get_gender_by_name(
    name="Michael",
    country="US",
    askToAI=False,
    forceToGenderize=False
)

print("Result for name 'Michael':")
print(result)

