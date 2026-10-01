from tools.file_analysis import FileAnalysisTool

tool = FileAnalysisTool()

print("Tool:", tool.name)
print("Description:", tool.description)

print("\nAnalyzing suspicious file...\n")

result = tool.run("invoice_update.exe")

print(result)