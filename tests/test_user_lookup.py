from tools.user_lookup import UserLookupTool

tool = UserLookupTool()

print("Tool:", tool.name)
print("Description:", tool.description)

print("\nLooking up bob...\n")

result = tool.run("bob")

print(result)