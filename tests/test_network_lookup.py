from tools.network_lookup import NetworkLookupTool

tool = NetworkLookupTool()

print("Tool:", tool.name)
print("Description:", tool.description)

print("\nInvestigating suspicious IP...\n")

result = tool.run("185.203.14.22")

print(result)