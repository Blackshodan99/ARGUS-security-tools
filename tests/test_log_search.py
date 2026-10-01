from tools.log_search import LogSearchTool

tool = LogSearchTool()

print("Tool:", tool.name)
print("Description:", tool.description)

print("\nSearching for bob...\n")

results = tool.run("bob")

for result in results:
    print(result)