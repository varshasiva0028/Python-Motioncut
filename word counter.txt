def count_words_and_letters(paragraph):
    if not paragraph.strip():
        print("Paragraph is empty. Please provide some input.")
        return
    words = paragraph.split()
    num_words = len(words)
    num_letters = sum(len(word) for word in words)
    print("Number of words:", num_words)
    print("Number of letters:", num_letters)
paragraph = input("Enter a paragraph: ")
count_words_and_letters(paragraph)