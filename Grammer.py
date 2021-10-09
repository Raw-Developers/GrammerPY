import language_check
  
  
# Mention the language keyword
tool = language_check.LanguageTool('en-US')
matches = []
  
# Path of file which needs to be checked
with open('transcript1.txt', 'r') as f:             
    for line in f:
        matches.extend(tool.check(line))

print("No. of mistakes found in document is", len(matches), "\n")
for mistake in matches:
    print(mistake, "\n")
