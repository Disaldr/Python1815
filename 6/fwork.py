# with open("text.txt") as file:
#     content = file.read()
#     print(content)

file_path = "text.txt"

fishtext = open(file_path)
content = fishtext.readlines()

print(content)
fishtext.close()