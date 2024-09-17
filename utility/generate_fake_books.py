from faker import Faker
import csv
import random
import argparse  # Import argparse for command-line argument parsing

fake = Faker()

def generate_fake_books(num_records, output_file):
    categories = [
        "Books > Fiction > Computers in Literature", 
        "Books > Fiction", 
        "Books > Non-Fiction > Essential programming"
    ]
  
    with open(output_file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        for _ in range(num_records):
            category = random.choice(categories)
            isbn = fake.isbn13(separator="")
            title = fake.catch_phrase()  # Generating fake book title
            description = fake.sentence(nb_words=15)
            partner = "Book partner"
            price = f"{round(random.uniform(1.99, 30.00), 2):.2f}"
            stock = random.randint(0, 100)
            
            csvwriter.writerow([
                "Book", category, isbn, title, description, 
                partner, isbn, price, stock
            ])
    print(f'{num_records} fake book records added to {output_file}.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate fake book records.")
    parser.add_argument('num_records', type=int, help="Number of fake book records to generate")
    parser.add_argument('output_file', type=str, help="Output file to store the fake book records")
    
    args = parser.parse_args()
    
    generate_fake_books(args.num_records, args.output_file)
