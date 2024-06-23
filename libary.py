### Problem Statement
""" Create a simple library management system where you have the following classes:

1. *Item*: Represents a general item in the library with attributes for title and publication year.
2. *Book*: Inherits from Item and adds specific attributes for author and ISBN.
3. *DVD*: Inherits from Item and adds specific attributes for director and duration.
4. *Library*: Manages a collection of items (books and DVDs), allowing adding, removing, and listing items.

### Requirements
1. *Item Class*
   - Attributes: title, publication_year
   - Method: get_info(): Returns a string with the title and publication year.

2. *Book Class*
   - Inherits from Item
   - Additional Attributes: author, ISBN
   - Method: Override get_info(): Returns a string with title, publication year, author, and ISBN.

3. *DVD Class*
   - Inherits from Item
   - Additional Attributes: director, duration
   - Method: Override get_info(): Returns a string with title, publication year, director, and duration.

4. *Library Class*
   - Attribute: items (a list to hold all library items)
   - Methods:
     - add_item(item): Adds a book or DVD to the library.
     - remove_item(item): Removes a book or DVD from the library.
     - list_items(): Prints information about all items in the library.

### Example Usage

1. Create instances of Book and DVD.
2. Add these items to a Library instance.
3. List all items in the library.
4. Remove an item from the library.
# 5. List items again to ensure the item was removed.

Write Python code to implement the above classes and demonstrate their functionality according to the requirements.

"""