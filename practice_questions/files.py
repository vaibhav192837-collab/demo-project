with open("practice_questions/example.txt", "w") as file:
    file.write("hello world")
print("File created and text written successfully.")

with open("practice_questions/example.txt","r") as file:
    data=file.read()
    print(data)