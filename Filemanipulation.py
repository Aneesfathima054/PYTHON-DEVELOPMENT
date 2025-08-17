filename = input("Enter the filename: ")
try:
    with open(filename, "r") as file:
        text = file.read().lower()  
    words = text.split()
    word_count = {}

    for word in words:
        
        word = "".join(c for c in word if c.isalnum())
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    for word in sorted(word_count):
        print(word, ":", word_count[word])
except FileNotFoundError:
    print("File not found. Please check the filename.")
