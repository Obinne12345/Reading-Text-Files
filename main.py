def read_file_content(filename):
    with open(filename) as file:
        text = file.read()
    return text
def count_words():
    text = read_file_content("./story.txt")
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = words.count(word)
    print(word_count)
    return word_count


count_words()   
