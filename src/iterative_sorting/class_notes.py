class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


# performs insertion sort to sort an array of books
def insertion_sort_by_title(arr_of_books):
    # iterate through the entire array
    # we can skip the first array element sinces theres nothing to compare to it
    # do we want to iterate over the books themselves or the indices???
    # we do need to have access to the book before the current book
    # we need access to each index in order to facilitate this sorting
    for i in range(1, len(arr_of_books)):
        curr_book = arr_of_books[i]
        # book index starts at i, but need ability to update it as we swap
        book_index = i
        #         prev_book = arr_of_books[i -1]

        # need to compare book with prev book
        # what do we compare by?
        while curr_book.title < arr_of_books[book_index - 1].title:
            # swap them
            arr_of_books[book_index], arr_of_books[book_index - 1] = arr_of_books[book_index - 1], arr_of_books[
                book_index]
            # we need to keep track of our current book's changing index
            book_index -= 1
    return arr_of_books


arr_of_books = [

    Book("Harry Potter and the Sorcerer's Stone", "JK Rowling", "Fantasy"),
    Book("Some Other Book", "Some Other Author", "Some Other Genre"),
    Book("Show Your Work", "Austin Kleon", "Self Help"),
    Book("The Lord of the Rings", "JRR Tolkien", "High Fantasy"),
    Book("Clean Code", "Robert J Martin", "Programming"),
    Book("The Rust of Programming Language", "Steve Klabnick and Carol Nichols", "Programming"),
    Book("The Way of Kings", "Brandon Sanderson", "High Fantasy"),

]