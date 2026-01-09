#!/usr/bin/env python
"""
Generate fake book data matching the format of sandbox/fixtures/books.essential.csv
"""
import csv
import random
from faker import Faker

fake = Faker()

# Define book categories
CATEGORIES = [
    "Books > Non-Fiction > Essential programming",
    "Books > Non-Fiction > Software Development",
    "Books > Non-Fiction > Computer Science",
    "Books > Fiction > Science Fiction",
    "Books > Fiction > Mystery",
    "Books > Fiction > Fantasy",
    "Books > Non-Fiction > Business",
    "Books > Non-Fiction > Technology",
]

# Common programming-related words for titles
TECH_WORDS = [
    "Programming", "Development", "Software", "Code", "Design", "Patterns",
    "Architecture", "Testing", "Agile", "Learning", "Mastering", "Advanced",
    "Introduction", "Guide", "Fundamentals", "Practical", "Professional",
    "Complete", "Essential", "Modern", "Clean", "Effective"
]

PROGRAMMING_LANGUAGES = [
    "Python", "Java", "JavaScript", "C++", "C#", "Ruby", "Go", "Rust",
    "PHP", "Swift", "Kotlin", "TypeScript", "Scala", "Haskell", "Perl"
]


def generate_tech_title():
    """Generate a programming/tech book title"""
    patterns = [
        lambda: f"{random.choice(TECH_WORDS)} {random.choice(PROGRAMMING_LANGUAGES)}",
        lambda: f"{random.choice(TECH_WORDS)} {random.choice(['Web', 'Mobile', 'Cloud', 'Database', 'Network'])} {random.choice(TECH_WORDS)}",
        lambda: f"The {random.choice(['Art', 'Science', 'Practice', 'Philosophy'])} of {random.choice(TECH_WORDS)}",
        lambda: f"{random.choice(PROGRAMMING_LANGUAGES)}: {random.choice(['The Complete Guide', 'A Practical Approach', 'Best Practices', 'From Beginner to Professional'])}",
    ]
    return random.choice(patterns)()


def generate_books_csv(filename='fake_books.csv', num_books=1000):
    """
    Generate a CSV file with fake book data matching the format:
    Type,Category,ISBN,Title,Description,Partner,Partner SKU,Price,Stock
    """

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        for _ in range(num_books):
            isbn = fake.isbn13()
            title = generate_tech_title()
            description = fake.text(max_nb_chars=250).replace('\n', ' ')
            category = random.choice(CATEGORIES)
            price = round(random.uniform(0.99, 29.99), 2)
            stock = random.randint(1, 99)

            row = [
                'Book',                # Type
                category,              # Category
                isbn,                  # ISBN
                title,                 # Title
                description,           # Description
                'Book partner',        # Partner
                isbn,                  # Partner SKU (same as ISBN)
                price,                 # Price
                stock                  # Stock
            ]

            writer.writerow(row)

    print(f'Generated {num_books} fake books in {filename}')


if __name__ == '__main__':
    import sys

    # Default to 1000 books, or use command line argument
    num_books = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'fake_books.csv'

    generate_books_csv(output_file, num_books)
