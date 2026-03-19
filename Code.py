def vertical_txt(text):
    words = text.split()
    max_len = max(len(word) for word in words)
    
    result = []
    
    for i in range(max_len):
        row = []
        for word in words:
            if i < len(word):
                row.append(word[i])
            else:
                row.append(" ")
        result.append(row)
    
    return result


# 👇 User input
user_input = input("Enter text: ")

# Generate and print result
output = vertical_txt(user_input)

for row in output:
    print(row)
