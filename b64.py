import base64

# Open the file in binary mode, read it, and encode it
with open('cases.js', 'rb') as file:
    base64_string = base64.b64encode(file.read()).decode()

print(base64_string)